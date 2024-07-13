from typing import Optional, Text

from pydantic import BaseModel, ConfigDict, Field

from seek_music.types.kkbox.territory import TerritoriesType


class SearchCall(BaseModel):
    model_config = ConfigDict(extra="forbid")
    q: Text = Field(
        ...,
        title="Search query keywords",
        description="Search query keywords, url encoded",
    )
    type: Text = Field(
        "track,album,artist,playlist",
        title="Types to search",
        description="Comma-separated list of types to search",
    )
    territory: TerritoriesType = Field(
        ...,
        title="Two-letter country codes",
        description="Two-letter country codes from ISO 3166-1 alpha-2",
    )
    offset: int = Field(
        0,
        title="Offset",
        description="The number of items to skip before starting to collect the result set",
        ge=0,
    )
    limit: int = Field(
        15,
        title="Limit",
        description="The number of items to return per page",
        ge=1,
        le=50,
    )
    availability: Optional[bool] = Field(
        None,
        title="Show only authorized result",
        description="Show only authorized result",
    )
