from typing import TYPE_CHECKING, Text

from seek_music.types.kkbox.territory import TerritoriesType
from seek_music.types.kkbox.track import Track
from seek_music.types.kkbox.track_data import TrackData
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class Tracks:
    PATH = "tracks"
    PATH_ID = "tracks/{track_id}"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    def list(self, ids: Text, territory: TerritoriesType) -> TrackData:
        base_url = self.parent.base_url
        url = str(base_url.with_path(join_paths(base_url.path, self.PATH)))
        headers = self.parent.headers
        params = {"ids": ids, "territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return TrackData.model_validate(res.json())

    def retrieve(self, track_id: Text, territory: TerritoriesType) -> Track:
        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(base_url.path, self.PATH_ID.format(track_id=track_id))
            )
        )
        headers = self.parent.headers
        params = {"territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return Track.model_validate(res.json())
