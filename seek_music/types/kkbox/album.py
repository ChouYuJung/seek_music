from typing import List

from pydantic import BaseModel, HttpUrl

from seek_music.types.kkbox.artist import Artist
from seek_music.types.kkbox.image import Image


class Album(BaseModel):
    id: str
    name: str
    url: HttpUrl
    explicitness: bool
    available_territories: List[str]
    release_date: str
    images: List[Image]
    artist: Artist
