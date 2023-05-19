from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

GENRE_CHOICES = [
    "POP", "ROCK","COUNTRY", "JAZZ", "R&B", "RAP"    
]


#create your models here
class Artist(models.Model):
    artist_name =  models.CharField(max_length=255)
    artist_genre =  models.CharField(max_length=255)

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    album_title =  models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_title

class Song(models.Model):
    song_title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.song_title

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        song_titles = self.songs.values_list('song_title', flat=True)
        return ', '.join(song_titles)

