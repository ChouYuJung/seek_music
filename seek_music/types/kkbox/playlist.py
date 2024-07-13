from typing import List, Optional, Text, Union

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from seek_music.types.kkbox.artist import Artist
from seek_music.types.kkbox.image import Image
from seek_music.types.kkbox.track_data import TrackData


class Playlist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    title: str
    description: str
    url: HttpUrl
    images: List[Image]
    updated_at: Union[Text, int]
    owner: Artist
    tracks: Optional[TrackData] = Field(None)
