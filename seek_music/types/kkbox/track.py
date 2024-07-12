from typing import List

from pydantic import BaseModel, HttpUrl

from seek_music.types.kkbox.album import Album


class Track(BaseModel):
    id: str
    name: str
    duration: int
    isrc: str
    url: HttpUrl
    track_number: int
    explicitness: bool
    available_territories: List[str]
    album: Album
