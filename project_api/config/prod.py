from .base import BaseConfig


class Config(BaseConfig):
    SQLALCHEMY_ECHO = False

    # Disable OpenAPI docs in Production
    OPENAPI_URL_PREFIX = None
