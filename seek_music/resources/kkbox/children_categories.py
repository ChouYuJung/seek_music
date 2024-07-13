from typing import TYPE_CHECKING, Text

from seek_music.types.kkbox.category_data import CategoryData, SubCategoryData
from seek_music.types.kkbox.playlist_data import PlaylistData
from seek_music.types.kkbox.territory import TerritoriesType
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class ChildrenCategories:
    PATH = "children-categories"
    PATH_ID = "children-categories/{category_id}"
    PATH_ID_PLAYLISTS = "children-categories/{category_id}/playlists"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    def list(
        self,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 20,
    ) -> "CategoryData":
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 20:
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
            return CategoryData.model_validate(res.json())

    def list_subcategories(
        self,
        category_id: Text,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 20,
    ) -> "SubCategoryData":
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 20:
            raise ValueError(
                "Value 'limit' must be greater than or equal to 1 "
                + "and less than or equal to 20"
            )
        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(base_url.path, self.PATH_ID.format(category_id=category_id))
            )
        )
        headers = self.parent.headers
        params = {"territory": territory}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return SubCategoryData.model_validate(res.json())

    def list_playlists(
        self,
        category_id: Text,
        territory: TerritoriesType,
        offset: int = 0,
        limit: int = 20,
    ) -> "PlaylistData":
        if offset < 0:
            raise ValueError("Value 'offset' must be greater than or equal to 0")
        if limit < 1 or limit > 20:
            raise ValueError(
                "Value 'limit' must be greater than or equal to 1 "
                + "and less than or equal to 50"
            )

        base_url = self.parent.base_url
        url = str(
            base_url.with_path(
                join_paths(
                    base_url.path,
                    self.PATH_ID_PLAYLISTS.format(category_id=category_id),
                )
            )
        )
        headers = self.parent.headers
        params = {"territory": territory, "offset": offset, "limit": limit}
        with self.parent.client.session as session:
            res = session.get(url, headers=headers, params=params)
            res.raise_for_status()
            return PlaylistData.model_validate(res.json())
