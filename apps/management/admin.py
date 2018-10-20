from django.contrib import admin
from .models import User,Songs,Albums,Artists,Album_Songs,Images,Favorites,Performed_By,Playlists,Sung_By

# Register your models here.
admin.site.register(User)
admin.site.register(Album_Songs)
admin.site.register(Albums)
admin.site.register(Artists)
admin.site.register(Images)
admin.site.register(Favorites)
admin.site.register(Performed_By)
admin.site.register(Playlists)
admin.site.register(Songs)
admin.site.register(Sung_By)