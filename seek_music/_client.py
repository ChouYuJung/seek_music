import httpx

from seek_music.resources.kkbox._client import KKBox

httpx.URL

__all__ = ["SeekMusic"]


class SeekMusic:
    kkbox: "KKBox"

    def __init__(self):
        self.kkbox = KKBox(self)

        self.http_client = httpx.Client()
        self.async_http_client = httpx.AsyncClient()
