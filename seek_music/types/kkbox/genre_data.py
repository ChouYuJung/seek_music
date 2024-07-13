from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.genre import Genre
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary


class GenreData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: List[Genre]
    paging: Optional[Paging] = Field(None)
    summary: Optional[Summary] = Field(None)
