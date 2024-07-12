from typing import List

from pydantic import BaseModel, ConfigDict, HttpUrl

from seek_music.types.kkbox.image import Image


class Artist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    url: HttpUrl
    images: List[Image]
