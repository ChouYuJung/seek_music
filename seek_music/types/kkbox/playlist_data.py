from typing import List

from pydantic import BaseModel

from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.playlist import Playlist
from seek_music.types.kkbox.summary import Summary


class PlaylistData(BaseModel):
    data: List[Playlist]
    paging: Paging
    summary: Summary
