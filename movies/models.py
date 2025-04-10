# movies/models.py
from django.db import models

class MpaaRating(models.Model):
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type} - {self.label}"

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.TextField()  # changed from CharField
    duration = models.IntegerField()
    genre = models.JSONField()
    language = models.CharField(max_length=50)
    mpaa_rating = models.ForeignKey(MpaaRating, on_delete=models.CASCADE)
    user_rating = models.IntegerField()

    def __str__(self):
        return self.name

