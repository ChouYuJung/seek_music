import os
from typing import TYPE_CHECKING, Optional, Text, Union

from httpx import URL

from seek_music.config import settings
from seek_music.resources.kkbox.oauth2 import Oauth2

if TYPE_CHECKING:
    from seek_music import SeekMusic


class KKBox:
    oauth2: "Oauth2"

    def __init__(
        self,
        client: "SeekMusic",
        *,
        base_url: Optional[Union[Text, URL]] = None,
        auth_base_url: Optional[Union[Text, URL]] = None,
        api_key: Optional[Text] = None
    ):
        self.client = client
        self._base_url = URL(base_url or "https://api.kkbox.com/v1.1")
        self._base_auth_url = URL(auth_base_url or "https://account.kkbox.com")

        __api_key = (
            api_key
            or os.environ.get("KKBOX_API_KEY")
            or os.environ.get("KKBOX_CLIENT_SECRET")
        )
        if __api_key is None:
            raise ValueError("Value 'api_key' is not set.")
        self.api_key_encrypted = settings.encrypt(__api_key)

        self.oauth2 = Oauth2(self)

    @property
    def base_url(self) -> URL:
        return self._base_url

    @property
    def base_auth_url(self) -> URL:
        return self._base_auth_url
