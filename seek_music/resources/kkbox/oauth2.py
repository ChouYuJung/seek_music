from typing import TYPE_CHECKING

from yarl import URL

from seek_music.resources.kkbox.token import Token
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox._client import KKBox


class Oauth2:
    PATH = "oauth2"

    token: Token

    def __init__(self, parent: "KKBox"):
        self.parent = parent

        self.token = Token(self)

    @property
    def url(self) -> URL:
        return self.parent.base_auth_url.with_path(
            path=join_paths(self.parent.base_auth_url.path, self.PATH)
        )
