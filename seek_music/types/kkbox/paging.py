from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class Paging(BaseModel):
    model_config = ConfigDict(extra="forbid")
    offset: int
    limit: int
    previous: Optional[HttpUrl]
    next: Optional[HttpUrl]
