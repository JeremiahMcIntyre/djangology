from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class Albums(models.Model):
    albumId = models.AutoField(primary_key=True)
    albumCoverPath = models.CharField(max_length=200, null=True)
    albumDuration = models.CharField(max_length=10, null=True)
    albumGenre = models.CharField(max_length=25)
    albumName = models.CharField(max_length=50)
    albumReleaseDateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.albumName

    class Meta:
        db_table = 'albums'

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, userDisplayName=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username, user_display_name=userDisplayName)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class Following(models.Model):
    userIdFk = models.IntegerField()
    followsIdFk = models.IntegerField()

    class Meta:
        db_table = 'following'
        unique_together = (('userIdFk', 'followsIdFk'),)


class Likes(models.Model):
    userIdFk = models.IntegerField()
    trackIdFk = models.IntegerField()
    likeDateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likes'
        unique_together = (('userIdFk', 'trackIdFk', 'likeDateTime'),)


class Playlists(models.Model):
    playlistCoverPath = models.CharField(max_length=200)
    playlistDateTime = models.DateTimeField(auto_now_add=True)
    playlistDuration = models.CharField(max_length=10, null=True)
    playlistId = models.AutoField(primary_key=True)
    playlistName = models.CharField(max_length=50)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.playlistName

    class Meta:
        db_table = 'playlists'


class PlaylistTracks(models.Model):
    trackIdFk = models.IntegerField()
    playlistIdFk = models.IntegerField()
    trackOrder = models.IntegerField()

    class Meta:
        db_table = 'playlistTracks'
        unique_together = (('trackIdFk', 'playlistIdFk'),)


class Tracks(models.Model):
    album = models.ForeignKey('Albums', on_delete=models.CASCADE)
    trackDuration = models.CharField(max_length=10, null=True)
    trackGenre = models.CharField(max_length=25)
    trackId = models.AutoField(primary_key=True)
    trackName = models.CharField(max_length=50)
    trackPath = models.CharField(max_length=200)

    def __str__(self):
        return self.trackName

    class Meta:
        db_table = 'tracks'




class Users(AbstractBaseUser):
    password = models.CharField(max_length=25)
    userId = models.AutoField(primary_key=True)
    userDisplayName = models.CharField(max_length=25)
    username = models.CharField(max_length=25, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['userId', 'password', 'userDisplayName']

    objects = CustomUserManager()


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


class UserTrack(models.Model):
    userIdFk = models.IntegerField()
    trackIdFk = models.IntegerField()
    playDateTime = models.DateTimeField()

    class Meta:
        db_table = 'userTracks'
        unique_together = (('userIdFk', 'trackIdFk', 'playDateTime'),)
