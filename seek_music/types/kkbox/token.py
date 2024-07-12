import math
import time
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, SecretStr, field_serializer


class Token(BaseModel):
    model_config = ConfigDict(extra="forbid")
    access_token: SecretStr
    token_type: Literal["Bearer"]
    expires_in: int
    created_at: int = Field(default_factory=lambda: math.ceil(time.time()))

    @field_serializer("access_token", when_used="always")
    def dump_secret(self, v: SecretStr):
        return v.get_secret_value()

    def is_expired(self) -> bool:
        return int(time.time()) > self.created_at + self.expires_in
