from typing import List, Optional

from pydantic import BaseModel, Field

from seek_music.types.kkbox.artist import Artist
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary


class ArtistData(BaseModel):
    data: List[Artist]
    paging: Optional[Paging] = Field(None)
    summary: Optional[Summary] = Field(None)
