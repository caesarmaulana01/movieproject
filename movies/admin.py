# movies/admin.py
from django.contrib import admin
from .models import Movie, MpaaRating

admin.site.register(Movie)
admin.site.register(MpaaRating)
