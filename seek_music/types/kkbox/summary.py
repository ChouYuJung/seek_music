from pydantic import BaseModel


class Summary(BaseModel):
    total: int
