from django.test import TestCase
from django.utils import timezone
from player.models import Albums, Following, Likes, Playlists, PlaylistTracks, Tracks, Users, UserTrack


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = Users.objects.create_user(username='testuser', password='password', userDisplayName='Test User')

        self.album = Albums.objects.create(albumCoverPath='path/to/album/cover.jpg', albumDuration='00:45:00',
                                            albumGenre='Rock', albumName='Test Album', user=self.user)

        self.track = Tracks.objects.create(album=self.album, trackDuration='00:04:30', trackGenre='Rock',
                                            trackName='Test Track', trackPath='path/to/track.mp3')

        self.playlist = Playlists.objects.create(playlistCoverPath='path/to/playlist/cover.jpg',
                                                  playlistDuration='01:30:00', playlistName='Test Playlist',
                                                  user=self.user)

    def test_user_creation(self):
        user_count = Users.objects.count()
        self.assertEqual(user_count, 1)

    def test_album_creation(self):
        album_count = Albums.objects.count()
        self.assertEqual(album_count, 1)

    def test_track_creation(self):
        track_count = Tracks.objects.count()
        self.assertEqual(track_count, 1)

    def test_playlist_creation(self):
        playlist_count = Playlists.objects.count()
        self.assertEqual(playlist_count, 1)

    def test_following_model(self):
        follow = Following.objects.create(userIdFk=self.user.userId, followsIdFk=self.user.userId)

        self.assertIsNotNone(follow)

    def test_likes_model(self):
        like = Likes.objects.create(userIdFk=self.user.userId, trackIdFk=self.track.trackId,
                                    likeDateTime=timezone.now())

        self.assertIsNotNone(like)

    def test_playlist_tracks_model(self):
        playlist_track = PlaylistTracks.objects.create(trackIdFk=self.track.trackId,
                                                        playlistIdFk=self.playlist.playlistId, trackOrder=1)

        self.assertIsNotNone(playlist_track)

    def test_user_track_model(self):
        user_track_play = UserTrack.objects.create(userIdFk=self.user.userId, trackIdFk=self.track.trackId,
                                                    playDateTime=timezone.now())

        self.assertIsNotNone(user_track_play)
