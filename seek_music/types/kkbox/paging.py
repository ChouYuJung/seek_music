from typing import Optional

from pydantic import BaseModel, HttpUrl


class Paging(BaseModel):
    offset: int
    limit: int
    previous: Optional[HttpUrl]
    next: Optional[HttpUrl]
