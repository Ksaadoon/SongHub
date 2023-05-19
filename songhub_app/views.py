from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, FormView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *

#create your views here (controllers)
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# routes for songhub 
def home(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    songs = Song.objects.all()

    context = {
        'artists': artists,
        'albums': albums,
        'songs': songs,         
    }
    return render(request, 'home.html', context)

def about(request):
  return render(request, 'about.html')

@login_required
def favoritesongs_index(request):
    favoritesongs = FavoriteSong.objects.filter(user=request.user)
    return render(request, 'favoritesongs/index.html', 
    { 
        'favoritesongs': favoritesongs
    }
)

@login_required
def favorite_detail(request, favoritesong_id):
    favoritesong = get_object_or_404(FavoriteSong, id=favoritesong_id)
    songs = favoritesong.songs.all()
    context = {
        'favoritesong': favoritesong,
        'songs': songs,
    }
    return render(request, 'favoritesongs/favorite_detail.html', context)


@login_required
def add_favorite(request):
    if request.method == 'POST' and 'song_id' in request.POST:
        song_id = request.POST['song_id']
        try:
            song = Song.objects.get(pk=song_id)

            # Check if the song is already in the user's favorites
            if not FavoriteSong.objects.filter(user=request.user, songs=song).exists():
                favorite_song = FavoriteSong.objects.create(user=request.user)
                favorite_song.songs.add(song)               
                return redirect('favorites')  # Redirect to the music list page (home)

        except Song.DoesNotExist:
            pass

    return redirect('favorites')


@login_required
def remove_favorite(request, favoritesong_id):
    if request.method == 'POST':
        favoritesong = get_object_or_404(FavoriteSong, id=favoritesong_id)
        if favoritesong.user == request.user:
            favoritesong.delete()
    return redirect('favorites')  # Redirect to the favorite songs page (index)

class MusicFormView(FormView):
    template_name = 'music/music_form.html'
    form_class = MusicForm
    success_url = '/'  # URL to redirect to after successful form submission

    def form_valid(self, form):
        # Save the form data
        artist_instance, album_instance, song_instance = form.save()       
        return super().form_valid(form)
    
