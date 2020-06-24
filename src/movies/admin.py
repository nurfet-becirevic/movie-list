from django.contrib import admin

# Register your models here.
from .models import Movie, Actor, UpdateTimeStamp

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(UpdateTimeStamp)
