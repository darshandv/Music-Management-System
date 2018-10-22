from django.contrib import admin
from .models import Song, Artist, Playlist, Album

# Register your models here.
# admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
# admin.site.register(Favorites)
# admin.site.register(Performed_By)
# admin.site.register(Playlists)
# admin.site.register(Songs)
# admin.site.register(Sung_By)
