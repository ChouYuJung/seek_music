from pydantic import BaseModel, ConfigDict, HttpUrl


class Image(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    width: int
    url: HttpUrl
