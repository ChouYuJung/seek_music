from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.image import Image
from seek_music.types.kkbox.track_data import TrackData


class Genre(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = Field(...)
    category: Optional[str] = Field(default=None)
    name: str = Field(...)
    tracks: Optional[TrackData] = Field(default=None)
    images: Optional[List[Image]] = Field(default=None)
