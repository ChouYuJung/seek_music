import requests

from seek_music.config import logger
from seek_music.resources.kkbox._client import KKBox

__all__ = ["SeekMusic"]


class SeekMusic:
    kkbox: "KKBox"

    def __init__(self):
        self.logger = logger
        self.session = requests.Session()

        self.kkbox = KKBox(self)
