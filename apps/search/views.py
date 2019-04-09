from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from apps.management.models import Song, Playlist

def is_paid(user):
    return user.groups.filter(name='Paid Clients').exists()

def is_platinum(user):
    return user.groups.filter(name='Platinum Users').exists()

User = get_user_model()
# Create your views here.
@login_required
def search(request):
    if 'q' in request.GET :
         query = request.GET.get('q')
         # users = User.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query),~Q(id = request.user.id))
         playlists = Playlist.objects.filter(user = request.user)

         user = request.user

         paid = False
         platinum = False
         if is_paid(user):
             paid = True

         if is_platinum(user):
             paid=True
             platinum = True


         songs = Song.objects.filter(song_title__icontains = query)
         return render (request, 'search/results.html', {'songs':songs, 'playlists':playlists, 'paid':paid, 'platinum':platinum})
    return render(request, 'search/error.html')
