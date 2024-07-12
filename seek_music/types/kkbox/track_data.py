from typing import List

from pydantic import BaseModel

from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary
from seek_music.types.kkbox.track import Track


class TrackData(BaseModel):
    data: List[Track]
    paging: Paging
    summary: Summary
