from .base import BaseConfig


class Config(BaseConfig):
    TESTING = True
    SQLALCHEMY_ECHO = False
