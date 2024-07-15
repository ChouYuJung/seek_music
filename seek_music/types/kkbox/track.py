from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from seek_music.types.kkbox.album import Album


class Track(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    duration: int
    isrc: Optional[str] = Field(default=None)
    url: HttpUrl
    track_number: int
    explicitness: bool
    available_territories: List[str]
    album: Optional[Album] = Field(default=None)
