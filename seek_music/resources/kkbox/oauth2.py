from typing import TYPE_CHECKING

from httpx import URL

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class Oauth2:
    path = "/oauth2"

    def __init__(self, parent: "KKBox"):
        self.parent = parent

    @property
    def url(self) -> URL:
        return self.parent.base_auth_url.join(self.path)
