from typing import List, Optional, Text

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.category import Category
from seek_music.types.kkbox.image import Image
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary


class CategoryData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: List[Category]
    paging: Optional[Paging] = Field(default=None)
    summary: Optional[Summary] = Field(default=None)
    greeting: Optional[Text] = Field(default=None)


class SubCategoryData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: Text
    title: Text
    images: List[Image]
    subcategories: Optional[List[Category]] = Field(default=None)
    paging: Optional[Paging] = Field(default=None)
    summary: Optional[Summary] = Field(default=None)
