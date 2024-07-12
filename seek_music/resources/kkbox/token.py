from typing import TYPE_CHECKING, Dict

from yarl import URL

from seek_music.config import logger, settings
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music.resources.kkbox.oauth2 import Oauth2


class Token:
    PATH = "token"

    def __init__(self, parent: "Oauth2"):
        self.parent = parent

    @property
    def url(self) -> URL:
        return self.parent.url.with_path(
            path=join_paths(self.parent.url.path, self.PATH)
        )

    def get(self) -> Dict:
        kkbox = self.parent.parent
        with kkbox.client.session as session:
            data = {
                "grant_type": "client_credentials",
                "client_id": kkbox.client_id,
                "client_secret": settings.decrypt(kkbox.api_key_encrypted),
            }
            logger.debug(f"Requesting token from {self.url!r}")
            res = session.post(str(self.url), data=data)
            res.raise_for_status()
            return res.json()
