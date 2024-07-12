from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.album_data import AlbumData
from seek_music.types.kkbox.artist_data import ArtistData
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.playlist_data import PlaylistData
from seek_music.types.kkbox.summary import Summary
from seek_music.types.kkbox.track_data import TrackData


class SearchResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tracks: Optional[TrackData] = Field(None)
    albums: Optional[AlbumData] = Field(None)
    artists: Optional[ArtistData] = Field(None)
    playlists: Optional[PlaylistData] = Field(None)
    summary: Optional[Summary] = Field(None)
    paging: Optional[Paging] = Field(None)
