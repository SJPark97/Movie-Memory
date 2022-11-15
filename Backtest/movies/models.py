from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    poster_URL = models.URLField(max_length=200)
    video_key = models.TextField(blank=True)
    release_date = models.TextField()
    overview = models.TextField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=30)
    popularity = models.FloatField()
    season = models.IntegerField(blank=True)
    weather = models.IntegerField(blank=True)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=50,blank=True)
    content = models.TextField(blank=True)
    # img = models.ImageField(blank=True, upload_to='item_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

