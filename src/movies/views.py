import requests

from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView
from datetime import datetime, timezone
from .models import Movie, Actor, UpdateTimeStamp


class MovieListView(ListView):
    def get(self, request):
        update_time = UpdateTimeStamp.objects.all()
        if len(update_time) > 0:
            td = datetime.utcnow().replace(tzinfo=timezone.utc) - update_time[0].last_update
            if td.seconds > settings.DB_REFRESH_INTERVAL_SECONDS:
                MovieListView._refresh_data(update_time[0])
        else:
            MovieListView._refresh_data(UpdateTimeStamp())

        context = {
            "movie_list": Movie.objects.all()
        }
        return render(request, "movies.html", context)

    @staticmethod
    def _refresh_data(timestamp):
        movie_actor = dict()
        response = requests.get(settings.API_BASE_URL + '/people')
        if response.status_code == 200:
            result = response.json()
            ids = Actor.objects.values_list('id', flat=True)
            actors = []
            for a in result:
                actor_id = a.get('id')
                if actor_id not in ids:
                    for f in a.get('films'):
                        movie_id = f[f.rfind('/') + 1:]
                        mar = movie_actor.get(movie_id)
                        if mar:
                            mar.add(actor_id)
                        else:
                            movie_actor[movie_id] = set([actor_id])

                    actors.append(Actor(
                        id=a.get('id'),
                        name=a.get('name')
                    ))
            if len(actors) > 0:
                Actor.objects.bulk_create(actors)
        else:
            print('status_code={}, url={}, message={}'.format(
                response.status_code, response.url, response.text))

        response = requests.get(settings.API_BASE_URL + '/films')
        if response.status_code == 200:
            result = response.json()
            ids = Movie.objects.values_list('id', flat=True)
            movies = []
            for m in result:
                if m.get('id') not in ids:
                    movies.append(Movie(
                        id=m.get('id'),
                        title=m.get('title'),
                        description=m.get('description'),
                        director=m.get('director'),
                        producer=m.get('producer'),
                        release_date=m.get('release_date'),
                        rt_score=m.get('rt_score'),
                    ))
            if len(movies) > 0:
                Movie.objects.bulk_create(movies)

                # populate many to many relational model
                through_model = Movie.people.through
                for key, value in movie_actor.items():
                    movie_actors = Actor.objects.filter(pk__in=list(value))
                    tm = [through_model(actor_id=actor.pk, movie_id=key) for actor in movie_actors]
                    through_model.objects.bulk_create(tm)

        else:
            print('status_code={}, url={}, message={}'.format(
                response.status_code, response.url, response.text))

            # skip refresh time update if requests failed
            return

        timestamp.save()
