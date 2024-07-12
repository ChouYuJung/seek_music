import logging
from typing import Optional, Text

from cryptography.fernet import Fernet
from pydantic import Field, PrivateAttr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOGGER_NAME: Text = "seek_music"
    FERNET_KEY: Optional[Text] = Field(default=None)

    _fernet: Optional[Fernet] = PrivateAttr(default=None)

    @property
    def fernet(self):
        if self._fernet is not None:
            return self._fernet
        if self.FERNET_KEY is None:
            raise ValueError("Value 'FERNET_KEY' is not set.")
        _fernet = Fernet(self.FERNET_KEY)
        return _fernet

    def encrypt(self, value: Text) -> Text:
        return self.fernet.encrypt(value.encode()).decode()

    def decrypt(self, value: Text) -> Text:
        return self.fernet.decrypt(value.encode()).decode()


settings = Settings()
logger = logging.getLogger(settings.LOGGER_NAME)
