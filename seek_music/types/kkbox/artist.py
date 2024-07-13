from typing import List, Optional, Text

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from seek_music.types.kkbox.image import Image


class Artist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    name: str
    url: HttpUrl
    images: List[Image]
    description: Optional[Text] = Field(default=None)
