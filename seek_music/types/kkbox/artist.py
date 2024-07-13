from typing import List, Optional, Text

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from seek_music.types.kkbox.image import Image


class Artist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    url: Optional[HttpUrl] = Field(default=None)
    images: Optional[List[Image]] = Field(default=None)
    description: Optional[Text] = Field(default=None)
