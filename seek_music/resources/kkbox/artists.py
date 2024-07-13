from typing import TYPE_CHECKING, Text

from seek_music.types.kkbox.album_data import AlbumData
from seek_music.types.kkbox.artist import Artist
from seek_music.types.kkbox.artist_data import ArtistData
from seek_music.types.kkbox.territory import TerritoriesType
from seek_music.types.kkbox.track_data import TrackData
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class Artists:
    PATH = "artists"
    PATH_ID = "/artists/{artist_id}"
    PATH_ID_ALBUMS = "/artists/{artist_id}/albums"
    PATH_ID_RELATED_ARTISTS = "/artists/{artist_id}/related-artists"
    PATH_ID_TOP_TRACKS = "/artists/{artist_id}/top-tracks"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    def retrieve(self, artist_id: Text, territory: TerritoriesType) -> "Artist":
        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(base_url.path, self.PATH_ID.format(artist_id=artist_id))
            )
        )
        headers = self.parent.headers
        params = {"territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return Artist.model_validate(res.json())

    def list_albums(
        self,
        artist_id: Text,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 100,
    ) -> "AlbumData":
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
                    base_url.path, self.PATH_ID_ALBUMS.format(artist_id=artist_id)
                )
            )
        )
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return AlbumData.model_validate(res.json())

    def list_related_artists(
        self,
        artist_id: Text,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 100,
    ) -> "ArtistData":
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 20:
            raise ValueError(
                "Value 'limit' must be greater than or equal to 1 "
                + "and less than or equal to 500"
            )

        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(
                    base_url.path,
                    self.PATH_ID_RELATED_ARTISTS.format(artist_id=artist_id),
                )
            )
        )
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return ArtistData.model_validate(res.json())

    def list_top_tracks(
        self,
        artist_id: Text,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 100,
    ) -> "TrackData":
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
                    base_url.path,
                    self.PATH_ID_TOP_TRACKS.format(artist_id=artist_id),
                )
            )
        )
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return TrackData.model_validate(res.json())
