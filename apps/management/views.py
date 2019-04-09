from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (DetailView, ListView, CreateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Playlist, Song, Album, Artist
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import (PlaylistForm, AddSongForm, AddArtistForm)
from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Artist

playlist_type = ContentType.objects.get_for_model(Playlist)
song_type = ContentType.objects.get_for_model(Song)

paid_clients, created = Group.objects.get_or_create(name='Paid Clients')
platinum_users, created = Group.objects.get_or_create(name='Platinum Users')


can_add_playlist_own, created = Permission.objects.get_or_create(codename='can_add_playlist_own',
    name='Can Add Playlist Own', content_type=playlist_type)


can_play_own, created = Permission.objects.get_or_create(codename='can_play_own',
    name='Can play Own', content_type=song_type)


# Add Paid permissions
paid_clients.permissions.add(can_play_own)

#Add Platinum permissions
platinum_users.permissions.add(can_play_own)
platinum_users.permissions.add(can_add_playlist_own)



class IndexView(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = 'management/user_home.html'
    # context_object_name = 'playlists'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlists = Playlist.objects.filter(user = self.request.user)

        user = self.request.user

        paid = False
        platinum = False

        if user.has_perm('management.can_add_playlist_own'):
            paid=True
            platinum = True

        context['paid'] = paid
        context['platinum'] = platinum
        context['playlists'] = playlists
        return context


class PlaylistCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'management:index'
    form_class = PlaylistForm
    template_name = 'management/playlist_form.html'
    model = Playlist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        paid = False
        platinum = False

        if user.has_perm('management.can_add_playlist_own'):
            paid=True
            platinum = True

        context['paid'] = paid
        context['platinum'] = platinum
        return context

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        initial['user'] = self.request.user

        return initial

class  PlaylistDeleteView(LoginRequiredMixin,DeleteView):
    model = Playlist
    success_url = reverse_lazy('management:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class AddSongView(LoginRequiredMixin,CreateView):
    model = Song
    form_class = AddSongForm

class AddArtistView(LoginRequiredMixin, PermissionRequiredMixin, CreateView ):
    model = Artist
    form_class = AddArtistForm
    permission_required ='management.can_add_artists'
    template_name = 'management/add_artist_form.html'

class ArtistListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Artist
    template_name = 'management/all_artists.html'
    permission_required ='management.can_view_artist';
    context_object_name = 'artists'


class SongsListView(LoginRequiredMixin,ListView):
    model = Song
    template_name = 'management/all_songs.html'
    context_object_name = 'songs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        playlists = Playlist.objects.filter(user = self.request.user)

        user = self.request.user

        paid = False
        platinum = False

        if user.has_perm('management.can_play'):
            paid=True

        if user.has_perm('management.can_add_playlist_own'):
            paid=True

        context['paid'] = paid
        context['platinum'] = platinum
        context['playlists'] = playlists
        return context

class AlbumsListView(LoginRequiredMixin,ListView):
    model = Album
    template_name = 'management/all_albums.html'
    context_object_name = 'albums'



class PlaylistDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'management/playlist_detail.html'
    context_object_name = 'playlist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_songs = Song.objects.exclude(part_of_playlist = self.get_object())
        context['new_songs'] = new_songs
        return context



class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'management/album_detail.html'
    context_object_name = 'album'


class FavoriteListView(LoginRequiredMixin,ListView):
    model = Song
    template_name = 'management/favorites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk = self.request.user.id)

        # for i in range(5):
        #     print('Python')
        # print(user.query.as_sql())
        songs = user.songs.all()
        context['songs'] = songs
        return context

@login_required
def add_favorite(request, song_id, user_id, playlist_id):
    song = get_object_or_404(Song, pk=song_id)
    user = get_object_or_404(User, pk=user_id)

    try:
        if song in user.songs.all():
            user.songs.remove(song)
        else:
            user.songs.add(song)

        user.save()

    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return HttpResponseRedirect(reverse('management:playlist_detail',args = [playlist_id]))

@login_required
def add_favorite_song(request, song_id, user_id):
    song = get_object_or_404(Song, pk=song_id)
    user = get_object_or_404(User, pk=user_id)

    if song in user.songs.all():
        user.songs.remove(song)
    else:
        user.songs.add(song)

    user.save()

    # print(connection.queries)




    return HttpResponseRedirect(reverse('management:all_songs'))

@login_required
def remove_favorite(request, song_id, user_id):
    song = get_object_or_404(Song, pk=song_id)
    user = get_object_or_404(User, pk=user_id)

    user.songs.remove(song)

    user.save()

    return HttpResponseRedirect(reverse('management:favorites'))


@login_required
def add_to_playlist(request, song_id, playlist_id):
    song = get_object_or_404(Song, pk=song_id)
    playlist = get_object_or_404(Playlist, pk=playlist_id)

    playlist.songs.add(song)

    playlist.save()

    return HttpResponse(status=204)

@login_required
def delete_from_playlist(request, song_id, playlist_id):
    song = get_object_or_404(Song, pk=song_id)
    playlist = get_object_or_404(Playlist, pk=playlist_id)

    playlist.songs.remove(song)

    playlist.save()

    return HttpResponseRedirect(reverse('management:playlist_detail',args = [playlist_id]))
