from typing import List

from pydantic import BaseModel, HttpUrl

from seek_music.types.kkbox.image import Image


class Artist(BaseModel):
    id: str
    name: str
    url: HttpUrl
    images: List[Image]
