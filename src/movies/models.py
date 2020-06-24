from django.db import models


class Actor(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.TextField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    director = models.TextField()
    producer = models.TextField()
    release_date = models.TextField()
    rt_score = models.TextField()
    people = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title


class UpdateTimeStamp(models.Model):
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.last_update)

