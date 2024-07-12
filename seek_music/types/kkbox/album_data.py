from typing import List

from pydantic import BaseModel

from seek_music.types.kkbox.album import Album
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary


class AlbumData(BaseModel):
    data: List[Album]
    paging: Paging
    summary: Summary
