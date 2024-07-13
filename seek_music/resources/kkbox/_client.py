import os
from typing import TYPE_CHECKING, Dict, Optional, Text, Union

from yarl import URL

from seek_music.config import settings
from seek_music.resources.kkbox.albums import Albums
from seek_music.resources.kkbox.artists import Artists
from seek_music.resources.kkbox.charts import Charts
from seek_music.resources.kkbox.children_categories import ChildrenCategories
from seek_music.resources.kkbox.featured_playlist_categories import (
    FeaturedPlaylistCategories,
)
from seek_music.resources.kkbox.featured_playlists import FeaturedPlaylists
from seek_music.resources.kkbox.genre_stations import GenreStations
from seek_music.resources.kkbox.mood_stations import MoodStations
from seek_music.resources.kkbox.new_hits_playlists import NewHitsPlaylists
from seek_music.resources.kkbox.new_release_categories import NewReleaseCategories
from seek_music.resources.kkbox.oauth2 import Oauth2
from seek_music.resources.kkbox.session_playlists import SessionPlaylists
from seek_music.resources.kkbox.shared_playlists import SharedPlaylists
from seek_music.resources.kkbox.tracks import Tracks
from seek_music.types.kkbox.search_call import SearchCall
from seek_music.types.kkbox.search_response import SearchResponse
from seek_music.types.kkbox.token import Token
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music import SeekMusic


class KKBox:
    """
    Implementation of the KKBox APIs:

    - [POST] https://account.kkbox.com/oauth2/token -> Token
    - [GET ] https://api.kkbox.com/v1.1/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/tracks/{track_id} -> Track
    - [GET ] https://api.kkbox.com/v1.1/albums/{albums_id} -> Album
    - [GET ] https://api.kkbox.com/v1.1/albums/{album_id}/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id} -> Artist
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}/albums -> AlbumData
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}/related-artists -> ArtistData
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}/top-tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/charts -> Charts
    - [GET ] https://api.kkbox.com/v1.1/charts/{playlist_id} -> PlaylistData
    - [GET ] https://api.kkbox.com/v1.1/charts/{playlist_id}/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/featured-playlists -> PlaylistData
    - [GET ] https://api.kkbox.com/v1.1/featured-playlists/{playlist_id} -> Playlist
    - [GET ] https://api.kkbox.com/v1.1/featured-playlists/{playlist_id}/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/new-hits-playlists -> PlaylistData
    - [GET ] https://api.kkbox.com/v1.1/new-hits-playlists/{playlist_id} -> Playlist
    - [GET ] https://api.kkbox.com/v1.1/new-hits-playlists/{playlist_id}/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/session-playlists -> PlaylistData
    - [GET ] https://api.kkbox.com/v1.1/session-playlists/{playlist_id} -> Playlist
    - [GET ] https://api.kkbox.com/v1.1/session-playlists/{playlist_id}/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/shared-playlists/{playlist_id} -> Playlist
    - [GET ] https://api.kkbox.com/v1.1/shared-playlists/{playlist_id}/tracks -> TrackData
    - [GET ] https://api.kkbox.com/v1.1/children-categories -> CategoryData
    - [GET ] https://api.kkbox.com/v1.1/children-categories/{category_id} -> SubCategoryData
    - [GET ] https://api.kkbox.com/v1.1/children-categories/{category_id}/playlists -> PlaylistData
    - [GET ] https://api.kkbox.com/v1.1/featured-playlist-categories -> CategoryData
    - [GET ] https://api.kkbox.com/v1.1/featured-playlist-categories/{category_id} -> Category
    - [GET ] https://api.kkbox.com/v1.1/featured-playlist-categories/{category_id}/playlists -> PlaylistData
    - [GET ] https://api.kkbox.com/v1.1/new-release-categories
    - [GET ] https://api.kkbox.com/v1.1/new-release-categories/{category_id}
    - [GET ] https://api.kkbox.com/v1.1/new-release-categories/{category_id}/albums
    - [GET ] https://api.kkbox.com/v1.1/genre-stations
    - [GET ] https://api.kkbox.com/v1.1/genre-stations/{station_id}
    - [GET ] https://api.kkbox.com/v1.1/mood-stations
    - [GET ] https://api.kkbox.com/v1.1/mood-stations/{station_id}
    """

    oauth2: "Oauth2"
    tracks: "Tracks"
    albums: "Albums"
    artists: "Artists"
    charts: "Charts"
    featured_playlists: "FeaturedPlaylists"
    new_hits_playlists: "NewHitsPlaylists"
    session_playlists: "SessionPlaylists"
    shared_playlists: "SharedPlaylists"
    children_categories: "ChildrenCategories"
    featured_playlist_categories: "FeaturedPlaylistCategories"
    new_release_categories: "NewReleaseCategories"
    genre_stations: "GenreStations"
    mood_stations: "MoodStations"

    PATH_SEARCH = "search"

    def __init__(
        self,
        client: "SeekMusic",
        *,
        base_url: Optional[Union[Text, URL]] = None,
        auth_base_url: Optional[Union[Text, URL]] = None,
        api_key: Optional[Text] = None,
    ):
        self.client = client
        self._base_url = URL(base_url or "https://api.kkbox.com/v1.1")
        self._base_auth_url = URL(auth_base_url or "https://account.kkbox.com")

        __client_id = os.environ.get("KKBOX_CLIENT_ID")
        __api_key = (
            api_key
            or os.environ.get("KKBOX_API_KEY")
            or os.environ.get("KKBOX_CLIENT_SECRET")
        )
        if __api_key is None:
            raise ValueError("Value 'api_key' is not set.")
        if __client_id is None:
            raise ValueError("Value 'client_id' is not set.")
        self.client_id = __client_id
        self.api_key_encrypted = settings.encrypt(__api_key)

        self.token: Optional["Token"] = None

        self.oauth2 = Oauth2(self)
        self.tracks = Tracks(self)
        self.albums = Albums(self)
        self.artists = Artists(self)
        self.charts = Charts(self)
        self.featured_playlists = FeaturedPlaylists(self)
        self.new_hits_playlists = NewHitsPlaylists(self)
        self.session_playlists = SessionPlaylists(self)
        self.shared_playlists = SharedPlaylists(self)
        self.children_categories = ChildrenCategories(self)
        self.featured_playlist_categories = FeaturedPlaylistCategories(self)
        self.new_release_categories = NewReleaseCategories(self)
        self.genre_stations = GenreStations(self)
        self.mood_stations = MoodStations(self)

    @property
    def base_url(self) -> URL:
        return self._base_url

    @property
    def base_auth_url(self) -> URL:
        return self._base_auth_url

    @property
    def headers(self) -> Dict:
        token = self.authenticate()
        return {
            "Authorization": f"{token.token_type} {token.access_token.get_secret_value()}",
        }

    def authenticate(self) -> "Token":
        if self.token is None or self.token.is_expired():
            self.token = self.oauth2.token.get()
            self.client.logger.debug(f"Authenticated with token {self.token!r}")
        return self.token

    def search(self, search_call: "SearchCall") -> "SearchResponse":
        url = str(
            self.base_url.with_path(join_paths(self.base_url.path, self.PATH_SEARCH))
        )
        headers = self.headers
        data = search_call.model_dump(exclude_none=True)
        with self.client.session as session:
            res = session.get(url, headers=headers, params=data)
            res.raise_for_status()
            return SearchResponse.model_validate(res.json())
