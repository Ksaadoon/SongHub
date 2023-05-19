from django.contrib import admin
from .models import *

#register your models here so we can manage them in admin
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(FavoriteSong)

