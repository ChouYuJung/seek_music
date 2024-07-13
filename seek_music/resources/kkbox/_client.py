import os
from typing import TYPE_CHECKING, Dict, Optional, Text, Union

from yarl import URL

from seek_music.config import settings
from seek_music.resources.kkbox.albums import Albums
from seek_music.resources.kkbox.artists import Artists
from seek_music.resources.kkbox.oauth2 import Oauth2
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

    - [POST] https://account.kkbox.com/oauth2/token
    - [GET ] https://api.kkbox.com/v1.1/tracks
    - [GET ] https://api.kkbox.com/v1.1/tracks/{track_id}
    - [GET ] https://api.kkbox.com/v1.1/albums
    - [GET ] https://api.kkbox.com/v1.1/albums/{albums_id}"
    - [GET ] https://api.kkbox.com/v1.1/albums/{album_id}/tracks
    - [GET ] https://api.kkbox.com/v1.1/artists
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}/albums
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}/related-artists
    - [GET ] https://api.kkbox.com/v1.1/artists/{artist_id}/top-tracks
    """

    oauth2: "Oauth2"
    tracks: "Tracks"
    albums: "Albums"
    artists: "Artists"
    # charts: "Charts"  # TODO: Implement charts
    # featured_playlists: "FeaturedPlaylists"  # TODO: Implement featured-playlists
    # new_hits_playlists: "NewHitsPlaylists"  # TODO: Implement new-hits-playlists
    # session_playlists: "SessionPlaylists"  # TODO: Implement session-playlists
    # shared_playlists: "SharedPlaylists"  # TODO: Implement shared-playlists
    # children_categories: "ChildrenCategories"  # TODO: Implement children-categories
    # featured_playlist_categories: "FeaturedPlaylistCategories"  # TODO: Implement featured-playlist-categories
    # new_release_categories: "NewReleaseCategories"  # TODO: Implement new-release-categories
    # genre_stations: "GenreStations"  # TODO: Implement genre-stations
    # mood_stations: "MoodStations"  # TODO: Implement mood-stations

    path_search = "search"

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
            self.base_url.with_path(join_paths(self.base_url.path, self.path_search))
        )
        headers = self.headers
        data = search_call.model_dump(exclude_none=True)
        with self.client.session as session:
            res = session.get(url, headers=headers, params=data)
            res.raise_for_status()
            return SearchResponse.model_validate(res.json())
