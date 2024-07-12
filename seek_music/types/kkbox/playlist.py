from typing import List

from pydantic import BaseModel, ConfigDict, HttpUrl

from seek_music.types.kkbox.artist import Artist
from seek_music.types.kkbox.image import Image


class Playlist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: str
    description: str
    url: HttpUrl
    images: List[Image]
    updated_at: str
    owner: Artist
