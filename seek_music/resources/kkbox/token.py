from typing import TYPE_CHECKING

from httpx import URL

if TYPE_CHECKING:
    from seek_music.resources.kkbox.oauth2 import Oauth2


class Token:
    path = "/token"

    def __init__(self, parent: "Oauth2"):
        self.parent = parent

    @property
    def url(self) -> URL:
        return self.parent.url.join(self.path)
