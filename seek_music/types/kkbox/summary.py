from pydantic import BaseModel, ConfigDict


class Summary(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
