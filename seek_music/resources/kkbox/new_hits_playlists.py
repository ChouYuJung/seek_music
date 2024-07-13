from typing import TYPE_CHECKING, Text

from seek_music.types.kkbox.playlist import Playlist
from seek_music.types.kkbox.playlist_data import PlaylistData
from seek_music.types.kkbox.territory import TerritoriesType
from seek_music.types.kkbox.track_data import TrackData
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class NewHitsPlaylists:
    PATH = "new-hits-playlists"
    PATH_ID = "new-hits-playlists/{playlist_id}"
    PATH_ID_TRACKS = "new-hits-playlists/{playlist_id}/tracks"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    def list(
        self,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 5,
    ) -> "PlaylistData":
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 10:
            raise ValueError(
                "Value 'limit' must be greater than or equal to 1 "
                + "and less than or equal to 50"
            )

        base_url = self.parent.base_url
        url = str(base_url.with_path(join_paths(base_url.path, self.PATH)))
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return PlaylistData.model_validate(res.json())

    def retrieve(self, playlist_id: Text, territory: TerritoriesType) -> "Playlist":
        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(base_url.path, self.PATH_ID.format(playlist_id=playlist_id))
            )
        )
        headers = self.parent.headers
        params = {"territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return Playlist.model_validate(res.json())

    def list_tracks(
        self,
        playlist_id: Text,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 100,
    ) -> TrackData:
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 500:
            raise ValueError(
                "Value 'limit' must be greater than or equal to 1 "
                + "and less than or equal to 500"
            )

        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(
                    base_url.path, self.PATH_ID_TRACKS.format(playlist_id=playlist_id)
                )
            )
        )
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return TrackData.model_validate(res.json())
