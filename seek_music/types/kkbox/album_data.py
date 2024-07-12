from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.album import Album
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary


class AlbumData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: List[Album]
    paging: Optional[Paging] = Field(None)
    summary: Optional[Summary] = Field(None)
