from typing import List, Text

from pydantic import BaseModel, ConfigDict

from seek_music.types.kkbox.image import Image


class Category(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: Text
    title: Text
    images: List[Image]
