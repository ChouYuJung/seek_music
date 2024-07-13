from typing import List, Optional, Text

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.album_data import AlbumData
from seek_music.types.kkbox.image import Image
from seek_music.types.kkbox.playlist_data import PlaylistData


class Category(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: Text
    title: Text
    images: Optional[List[Image]] = Field(default=None)
    playlists: Optional[PlaylistData] = Field(default=None)
    albums: Optional[AlbumData] = Field(default=None)
