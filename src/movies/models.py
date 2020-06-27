from django.db import models


class Actor(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    release_date = models.PositiveIntegerField()
    rt_score = models.PositiveIntegerField()
    people = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title


class UpdateTimeStamp(models.Model):
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.last_update)

