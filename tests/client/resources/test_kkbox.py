from seek_music import SeekMusic
from seek_music.types.kkbox.search_call import SearchCall
from seek_music.utils._time import delay

DELAY_TIME = 2.0

test_track_id = "KsNxNkw3fpSTS3_hs4"
test_album_id = "GlEKlHUQs-18CGgUZs"
test_artist_id = "GtjT_E-Fw6HSCE7jgQ"
test_playlist_id = "4rqDCd_49kvNhHZ5-b"


sm = SeekMusic()


def test_kkbox_resources_search():
    # Test search
    with delay(DELAY_TIME):
        search_call = SearchCall(
            q="周杰倫",
            type="track,album,artist,playlist",
            territory="TW",
            offset=0,
            limit=1,
        )
        search_res = sm.kkbox.search(search_call)
        assert search_res.tracks
        assert search_res.albums
        assert search_res.artists
        assert search_res.playlists


def test_kkbox_resources_tracks():
    # Test tracks
    with delay(DELAY_TIME):
        track = sm.kkbox.tracks.list(ids=test_track_id, territory="TW")
        assert track.data[0].id == test_track_id
    with delay(DELAY_TIME):
        track = sm.kkbox.tracks.retrieve(test_track_id, territory="TW")
        assert track.id == test_track_id


def test_kkbox_resources_albums():
    # Test albums
    with delay(DELAY_TIME):
        album = sm.kkbox.albums.retrieve(test_album_id, territory="TW")
        assert album.id == test_album_id
    with delay(DELAY_TIME):
        album = sm.kkbox.albums.list_tracks(test_album_id, territory="TW", limit=1)
        assert album.data[0].album
        assert album.data[0].album.id == test_album_id


def test_kkbox_resources_artists():
    # Test artists
    with delay(DELAY_TIME):
        artist = sm.kkbox.artists.retrieve(test_artist_id, territory="TW")
        assert artist.id == test_artist_id
    with delay(DELAY_TIME):
        artist = sm.kkbox.artists.list_albums(test_artist_id, territory="TW", limit=1)
        assert artist.data[0].artist
        assert artist.data[0].artist.id == test_artist_id
    with delay(DELAY_TIME):
        artist = sm.kkbox.artists.list_related_artists(
            test_artist_id, territory="TW", limit=1
        )
        assert artist.data
    with delay(DELAY_TIME):
        artist = sm.kkbox.artists.list_top_tracks(
            test_artist_id, territory="TW", limit=1
        )
        assert artist.data[0].album
        assert artist.data[0].album.artist.id == test_artist_id
