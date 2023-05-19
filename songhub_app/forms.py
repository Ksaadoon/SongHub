
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
            # Check if the artist already exists
            artist = Artist.objects.get(artist_name=artist_name)
        except ObjectDoesNotExist:
            # Create a new artist if it doesn't exist
            artist = Artist.objects.create(artist_name=artist_name, artist_genre=artist_genre)

        try:
            # Check if the album already exists
            album = Album.objects.get(album_title=album_title, artist=artist)
        except ObjectDoesNotExist:
            # Create a new album if it doesn't exist
            album = Album.objects.create(album_title=album_title, artist=artist)

        try:
            # Check if the song already exists
            song = Song.objects.get(song_title=song_title, album=album)
        except ObjectDoesNotExist:
            # Create a new song if it doesn't exist
            song = Song.objects.create(song_title=song_title, album=album)

        return artist, album, song