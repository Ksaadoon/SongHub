from django.urls import path
from .views import signup, MusicFormView, about, home,favoritesongs_index, add_favorite, remove_favorite, favorite_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    
    path('songhub/', favoritesongs_index, name='favorites'),
    path('songhub/add_favorite/', add_favorite, name='add_favorite'),    
    path('songhub/favorite_detail/<int:favoritesong_id>/', favorite_detail, name='favorite_detail'),
    path('favorites/remove/<int:favoritesong_id>/', remove_favorite, name='remove_favorite'),
    
    path('songhub/music/', MusicFormView.as_view(), name='music_form'),
    
    path('accounts/signup/', signup, name='signup'),

]