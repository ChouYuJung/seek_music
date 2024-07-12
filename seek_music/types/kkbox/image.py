from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    height: int
    width: int
    url: HttpUrl
