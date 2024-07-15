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


def test_kkbox_resources_charts():
    # Test charts
    with delay(DELAY_TIME):
        playlists = sm.kkbox.charts.list(territory="TW", limit=1)
        assert playlists.data
        test_playlist_id = playlists.data[0].id  # Reset test_playlist_id
    with delay(DELAY_TIME):
        charts = sm.kkbox.charts.retrieve(test_playlist_id, territory="TW")
        assert charts.id == test_playlist_id
    with delay(DELAY_TIME):
        charts = sm.kkbox.charts.list_tracks(test_playlist_id, territory="TW", limit=1)
        assert charts.data[0].album


def test_kkbox_resources_featured_playlists():
    # Test featured playlists
    with delay(DELAY_TIME):
        playlists = sm.kkbox.featured_playlists.list(territory="TW", limit=1)
        assert playlists.data
        test_playlist_id = playlists.data[0].id  # Reset test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.featured_playlists.retrieve(
            test_playlist_id, territory="TW"
        )
        assert playlists.id == test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.featured_playlists.list_tracks(
            test_playlist_id, territory="TW", limit=1
        )
        assert playlists.data[0].album


def test_kkbox_resources_new_hits_playlists():
    # Test new hits playlists
    with delay(DELAY_TIME):
        playlists = sm.kkbox.new_hits_playlists.list(territory="TW", limit=1)
        assert playlists.data
        test_playlist_id = playlists.data[0].id  # Reset test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.new_hits_playlists.retrieve(
            test_playlist_id, territory="TW"
        )
        assert playlists.id == test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.new_hits_playlists.list_tracks(
            test_playlist_id, territory="TW", limit=1
        )
        assert playlists.data[0].album


def test_kkbox_resources_session_playlists():
    # Test session playlists
    with delay(DELAY_TIME):
        playlists = sm.kkbox.session_playlists.list(territory="TW", limit=1)
        assert playlists.data
        test_playlist_id = playlists.data[0].id  # Reset test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.session_playlists.retrieve(
            test_playlist_id, territory="TW"
        )
        assert playlists.id == test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.session_playlists.list_tracks(
            test_playlist_id, territory="TW", limit=1
        )
        assert playlists.data[0].album


def test_kkbox_resources_shared_playlists():
    # Test shared playlists
    test_playlist_id = "4nUZM-TY2aVxZ2xaA-"
    with delay(DELAY_TIME):
        playlists = sm.kkbox.shared_playlists.retrieve(test_playlist_id, territory="TW")
        assert playlists.id == test_playlist_id
    with delay(DELAY_TIME):
        playlists = sm.kkbox.shared_playlists.list_tracks(
            test_playlist_id, territory="TW", limit=1
        )
        assert playlists.data[0].album


def test_kkbox_resources_children_categories():
    # Test children categories
    with delay(DELAY_TIME):
        categories = sm.kkbox.children_categories.list(territory="TW", limit=1)
        assert categories.data
        test_category_id = categories.data[0].id  # Set test_category_id
    with delay(DELAY_TIME):
        sub_categories = sm.kkbox.children_categories.list_subcategories(
            test_category_id, territory="TW", limit=1
        )
        assert sub_categories.id == test_category_id
    with delay(DELAY_TIME):
        categories = sm.kkbox.children_categories.list_playlists(
            test_category_id, territory="TW", limit=1
        )
        assert categories.data


def test_kkbox_resources_featured_playlist_categories():
    # Test featured playlist categories
    with delay(DELAY_TIME):
        categories = sm.kkbox.featured_playlist_categories.list(territory="TW", limit=1)
        assert categories.data
        test_category_id = categories.data[0].id  # Set test_category_id
    with delay(DELAY_TIME):
        categories = sm.kkbox.featured_playlist_categories.retrieve(
            test_category_id, territory="TW"
        )
        assert categories.id == test_category_id
    with delay(DELAY_TIME):
        categories = sm.kkbox.featured_playlist_categories.list_playlists(
            test_category_id, territory="TW", limit=1
        )


def test_kkbox_resources_new_release_categories():
    # Test new release categories
    with delay(DELAY_TIME):
        categories = sm.kkbox.new_release_categories.list(territory="TW", limit=1)
        assert categories.data
        test_category_id = categories.data[0].id  # Set test_category_id
    with delay(DELAY_TIME):
        categories = sm.kkbox.new_release_categories.retrieve(
            test_category_id, territory="TW"
        )
        assert categories.id == test_category_id
    with delay(DELAY_TIME):
        categories = sm.kkbox.new_release_categories.list_albums(
            test_category_id, territory="TW", limit=20
        )
        assert categories.data
