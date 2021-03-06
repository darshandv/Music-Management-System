from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()



# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'artist_images')




    def __str__(self):
        return self.name

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'playlist_images')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("management:playlist_detail", args=[self.pk])

class Album(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE )
    name = models.CharField(max_length = 250)
    release_date = models.DateField()
    image = models.ImageField(upload_to = 'album_images')
    favorite_of = models.ManyToManyField(User, blank = True)

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name='songs')
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField()
    part_of_playlist = models.ManyToManyField(Playlist, blank = True, related_name = 'songs')
    favorite_of = models.ManyToManyField(User, blank = True, related_name='songs')

    def __str__(self):
        return self.song_title





# class Songs(models.Model):
#     song_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=30)
#     length = models.IntegerField()
#     genre = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.title
#
# class User(models.Model):
#     email_id = models.EmailField(primary_key=True)
#     first_name=models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.first_name+self.last_name
#
# class Images(models.Model):
#     image_id = models.AutoField(primary_key=True)
#     image_location = models.CharField(max_length=30)
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
# class Artists(models.Model):
#     artist_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     total_songs = models.IntegerField()
#     total_albums = models.IntegerField()
#     image_id = models.OneToOneField(Images,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
# class Albums(models.Model):
#     album_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     release_date = models.DateField()
#     album_length = models.IntegerField()
#     image = models.OneToOneField    (Images,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
# class Playlists(models.Model):
#     playlist = models.IntegerField()
#     song = models.ForeignKey(Songs,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#
#     class Meta:
#         unique_together = (('playlist','song','user'),)
#
# class Favorites(models.Model):
#     song = models.ForeignKey(Songs,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = (('song','user'),)
#
#
# class Album_Songs(models.Model):
#     album = models.ForeignKey(Albums,on_delete=models.CASCADE)
#     song = models.ForeignKey(Songs,on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = (('album','song'),)
#
# class Sung_By(models.Model):
#     song = models.ForeignKey(Songs,on_delete=models.CASCADE)
#     artist=models.ForeignKey(Artists,on_delete=models.CASCADE)
#
#     class Meta :
#         unique_together = (('song','artist'),)
#
#
# class Performed_By(models.Model):
#     album = models.ForeignKey(Albums,on_delete=models.CASCADE)
#     artist = models.ForeignKey(Artists,on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = (('album', 'artist'),)
