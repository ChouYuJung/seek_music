from pydantic import BaseModel

from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.summary import Summary
from seek_music.types.kkbox.track_data import TrackData


class SearchResponse(BaseModel):
    tracks: TrackData
    summary: Summary
    paging: Paging
