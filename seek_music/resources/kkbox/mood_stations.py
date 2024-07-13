from typing import TYPE_CHECKING, Text

from seek_music.types.kkbox.genre_data import Genre, GenreData
from seek_music.types.kkbox.territory import TerritoriesType
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class MoodStations:
    PATH = "mood-stations"
    PATH_ID = "mood-stations/{station_id}"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    def list(
        self, territory: TerritoriesType, offset: int = 0, limit: int = 50
    ) -> "GenreData":
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 500:
            raise ValueError(
                "Value 'limit' must be greater than or equal to 1 "
                + "and less than or equal to 500"
            )

        base_url = self.parent.base_url
        url = str(base_url.with_path(join_paths(base_url.path, self.PATH)))
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return GenreData.model_validate(res.json())

    def retrieve(self, station_id: Text, territory: TerritoriesType) -> "Genre":
        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(base_url.path, self.PATH_ID.format(station_id=station_id))
            )
        )
        headers = self.parent.headers
        params = {"territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return Genre.model_validate(res.json())
