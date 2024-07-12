from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary
from seek_music.types.kkbox.track import Track


class TrackData(BaseModel):
    model_config = ConfigDict(extra="forbid")
    data: List[Track]
    paging: Optional[Paging] = Field(None)
    summary: Optional[Summary] = Field(None)
