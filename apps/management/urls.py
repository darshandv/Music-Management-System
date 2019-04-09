from django.conf.urls import url, include
from django.urls import reverse
from . import views

app_name = 'management'

urlpatterns = [
url(r'^index/', views.IndexView.as_view(), name = 'index'),
url(r'^addplaylist/', views.PlaylistCreateView.as_view(), name = 'playlist_add'),
url(r'^addartist/', views.AddArtistView.as_view(), name = 'artist_add'),
url(r'^playlist/(?P<pk>\d+)/', views.PlaylistDetailView.as_view(), name = 'playlist_detail'),
url(r'^favorite/(?P<song_id>\d+)/(?P<user_id>\d+)/(?P<playlist_id>\d+)/', views.add_favorite, name = 'add_favorite'),
url(r'^favorite/(?P<song_id>\d+)/(?P<user_id>\d+)/', views.add_favorite_song, name = 'add_favorite_song'),
url(r'^allsongs', views.SongsListView.as_view(), name = 'all_songs'),
url(r'^allartists', views.ArtistListView.as_view(), name = 'all_artists'),
url(r'^favorites', views.FavoriteListView.as_view(), name = 'favorites'),
url(r'^remove_favorite/(?P<song_id>\d+)/(?P<user_id>\d+)/', views.remove_favorite, name = 'remove_favorite'),
url(r'^delete_from_playlist/(?P<song_id>\d+)/(?P<playlist_id>\d+)/', views.delete_from_playlist, name = 'delete_from_playlist'),
url(r'^addtoplaylist/(?P<song_id>\d+)/(?P<playlist_id>\d+)/', views.add_to_playlist, name = 'add_to_playlist'),
url(r'^allalbums/', views.AlbumsListView.as_view(), name = 'all_albums'),
url(r'^album/(?P<pk>\d+)/', views.AlbumDetailView.as_view(), name = 'album_detail'),
url(r'^deleteplaylist/(?P<pk>\d+)/', views.PlaylistDeleteView.as_view(), name = 'delete_playlist'),
]
