from django.test import TestCase
from .models import Movie, Actor, UpdateTimeStamp


class MovieTestCase(TestCase):
    def setUp(self):
        self.m1 = Movie.objects.create(
            id='1234-5678-abcd',
            title='Falling Star',
            description='Falling Star desc',
            director='John Doe',
            producer='Somebody',
            release_date=2019,
            rt_score=95,
        )
        self.m2 = Movie.objects.create(
            id='6789-abcd-0123',
            title='Final Fantasy',
            description='Final Fantasy desc',
            director='James Bond',
            producer='Sosuke',
            release_date=2020,
            rt_score=91,
        )
        self.a1 = Actor.objects.create(id='1321-1322', name='Kawasaki')
        self.a2 = Actor.objects.create(id='5677-6789', name='Honda')

        self.m1.people.add(self.a1)
        self.m1.people.add(self.a2)

    def test_movies(self):
        m1 = Movie.objects.get(id=self.m1.id)
        m2 = Movie.objects.get(id=self.m2.id)
        self.assertEqual(m1.title, self.m1.title)
        self.assertEqual(m1.description, self.m1.description)
        self.assertEqual(m1.director, self.m1.director)
        self.assertEqual(m1.producer, self.m1.producer)
        self.assertEqual(m1.release_date, self.m1.release_date)
        self.assertEqual(m1.rt_score, self.m1.rt_score)
        self.assertEqual(m2.title, self.m2.title)

        self.assertEqual(len(m1.people.all()), 2, "Movie should have people")


class ActorTestCase(TestCase):
    def setUp(self):
        self.a1 = Actor.objects.create(id='1321-1322', name='Kawasaki')
        self.a2 = Actor.objects.create(id='5677-6789', name='Honda')

    def test_actors(self):
        actor = Actor.objects.get(id=self.a1.id)
        self.assertEqual(self.a1.name, actor.name)
        actor = Actor.objects.get(id=self.a2.id)
        self.assertEqual(self.a2.name, actor.name)


class UpdateTimeStampTestCase(TestCase):
    def setUp(self):
        UpdateTimeStamp().save()

    def test_update_time_auto_create(self):
        """UpdateTimeStamp last_update field must auto create/update to datetime.now()"""
        query_set = UpdateTimeStamp.objects.all()
        self.assertTrue(len(query_set) == 1)

        t1 = query_set[0].last_update
        query_set[0].save()

        query_set = UpdateTimeStamp.objects.all()
        self.assertGreater(query_set[0].last_update, t1)
