import os
from typing import TYPE_CHECKING, Dict, Optional, Text, Union

from yarl import URL

from seek_music.config import settings
from seek_music.resources.kkbox.oauth2 import Oauth2
from seek_music.types.kkbox.search_response import SearchResponse
from seek_music.types.kkbox.token import Token
from seek_music.utils.url import join_paths

if TYPE_CHECKING:
    from seek_music import SeekMusic


class KKBox:
    oauth2: "Oauth2"

    path_search = "search"

    def __init__(
        self,
        client: "SeekMusic",
        *,
        base_url: Optional[Union[Text, URL]] = None,
        auth_base_url: Optional[Union[Text, URL]] = None,
        api_key: Optional[Text] = None,
    ):
        self.client = client
        self._base_url = URL(base_url or "https://api.kkbox.com/v1.1")
        self._base_auth_url = URL(auth_base_url or "https://account.kkbox.com")

        __client_id = os.environ.get("KKBOX_CLIENT_ID")
        __api_key = (
            api_key
            or os.environ.get("KKBOX_API_KEY")
            or os.environ.get("KKBOX_CLIENT_SECRET")
        )
        if __api_key is None:
            raise ValueError("Value 'api_key' is not set.")
        if __client_id is None:
            raise ValueError("Value 'client_id' is not set.")
        self.client_id = __client_id
        self.api_key_encrypted = settings.encrypt(__api_key)

        self.token: Optional["Token"] = None

        self.oauth2 = Oauth2(self)

    @property
    def base_url(self) -> URL:
        return self._base_url

    @property
    def base_auth_url(self) -> URL:
        return self._base_auth_url

    @property
    def headers(self) -> Dict:
        token = self.authenticate()
        return {
            "Authorization": f"{token.token_type} {token.access_token.get_secret_value()}",
        }

    def authenticate(self) -> "Token":
        if self.token is None or self.token.is_expired():
            self.token = self.oauth2.token.get()
            self.client.logger.debug(f"Authenticated with token {self.token!r}")
        return self.token

    def search(self) -> "SearchResponse":
        url = str(
            self.base_url.with_path(join_paths(self.base_url.path, self.path_search))
        )
        headers = self.headers
        with self.client.session as session:
            res = session.get(
                url,
                headers=headers,
                params={
                    "q": "Different World",
                    "type": "track",
                    "territory": "TW",
                },
            )
            res.raise_for_status()
            return SearchResponse.model_validate(res.json())
