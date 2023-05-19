
from django import forms
from django.forms import BaseForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name', 'artist_genre']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_title']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title']

class MusicForm(forms.Form):
    artist_name = forms.CharField(max_length=255)
    artist_genre = forms.CharField(max_length=255)
    album_title = forms.CharField(max_length=255)
    song_title = forms.CharField(max_length=255)

    def save(self):
        artist_name = self.cleaned_data['artist_name']
        artist_genre = self.cleaned_data['artist_genre']
        album_title = self.cleaned_data['album_title']
        song_title = self.cleaned_data['song_title']

        try:
            artist = Artist.objects.get(artist_name=artist_name)
        except ObjectDoesNotExist:
            artist = Artist.objects.create(artist_name=artist_name, artist_genre=artist_genre)

        try:
            album = Album.objects.get(album_title=album_title, artist=artist)
        except ObjectDoesNotExist:
            album = Album.objects.create(album_title=album_title, artist=artist)

        # handling ManyToManyField
        songs = []
        for title in song_title.split(','):
            song, created = Song.objects.get_or_create(song_title=title.strip(), album=album)
            songs.append(song)

        user = self.request.user
        # Update or create FavoriteSong instance
        favoritesong, created = FavoriteSong.objects.get_or_create(user=user)
        favoritesong.songs.set(songs)  # Update the songs relationship

        return artist, album, songs

