from typing import List

from pydantic import BaseModel

from seek_music.types.kkbox.artist import Artist
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary


class ArtistData(BaseModel):
    data: List[Artist]
    paging: Paging
    summary: Summary
