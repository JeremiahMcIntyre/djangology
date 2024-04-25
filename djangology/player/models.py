from django.db import models


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


class Following(models.Model):
    userIdFk = models.IntegerField(primary_key=True)
    followsIdFk = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'following'


class Likes(models.Model):
    userIdFk = models.IntegerField(primary_key=True)
    trackIdFk = models.IntegerField(primary_key=True)
    likeDateTime = models.DateTimeField(primary_key=True, auto_now_add=True)

    class Meta:
        db_table = 'likes'


class Playlists(models.Model):
    playlistCoverPath = models.CharField(max_length=200)
    playlistDateTime = models.DateTimeField(auto_now_add=True)
    playlistDuration = models.CharField(max_length=10, null=True)
    playlistId = models.AutoField(primary_key=True)
    playlistName = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

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


class Users(models.Model):
    password = models.CharField(max_length=25)
    userId = models.AutoField(primary_key=True)
    userDisplayName = models.CharField(max_length=25)
    username = models.CharField(max_length=25)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


class UserTracks(models.Model):
    userIdFk = models.IntegerField(primary_key=True)
    trackIdFk = models.IntegerField(primary_key=True)
    playDateTime = models.DateTimeField(primary_key=True, auto_now_add=True)

    class Meta:
        db_table = 'userTracks'
