from pydantic import BaseModel

from seek_music.types.kkbox.album_data import AlbumData
from seek_music.types.kkbox.artist_data import ArtistData
from seek_music.types.kkbox.paging import Paging
from seek_music.types.kkbox.playlist_data import PlaylistData
from seek_music.types.kkbox.summary import Summary
from seek_music.types.kkbox.track_data import TrackData


class SearchResponse(BaseModel):
    tracks: TrackData
    albums: AlbumData
    artists: ArtistData
    playlists: PlaylistData
    summary: Summary
    paging: Paging
