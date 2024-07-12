from typing import TYPE_CHECKING, Literal, Text

from seek_music.types.kkbox.track_data import TrackData
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class Tracks:
    PATH = "tracks"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    def list(
        self, ids: Text, territory: Literal["HK", "JP", "MY", "SG", "TW"]
    ) -> TrackData:
        base_url = self.parent.base_url
        url = str(base_url.with_path(join_paths(base_url.path, self.PATH)))
        headers = self.parent.headers
        params = {"ids": ids, "territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return TrackData.model_validate(res.json())
