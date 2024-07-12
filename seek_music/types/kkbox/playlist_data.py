from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.playlist import Playlist
from seek_music.types.kkbox.summary import Summary


class PlaylistData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: List[Playlist]
    paging: Optional[Paging] = Field(None)
    summary: Optional[Summary] = Field(None)
