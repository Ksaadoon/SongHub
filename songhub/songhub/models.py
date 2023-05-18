from django.db import models

#create your models here
class User(models.Model):
    username =  models.CharField(max_length=255)
    email =  models.CharField(max_length=255)

    def __str_(self):
        return self.email

class Artist(models.Model):
    artist_name =  models.CharField(max_length=255)
    artist_genre =  models.CharField(max_length=255)
    artist_country =  models.CharField(max_length=255)

    def __str_(self):
        return self.artist_name

class Album(models.Model):
    album_title =  models.CharField(max_length=255)
    release_date = models.DateField
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str_(self):
        return self.album_title

class Song(models.Model):
    song_title = models.CharField(max_length=255)
    duration = models.IntegerField
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str_(self):
        return self.song_title

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str_(self):
        return self.song



