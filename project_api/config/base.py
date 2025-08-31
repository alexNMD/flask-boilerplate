import os


class BaseConfig:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # https://flask-sqlalchemy.palletsprojects.com/en/stable/config/
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # OpenAPI / Swagger settings
    # https://flask-smorest.readthedocs.io/en/latest/openapi.html
    API_TITLE = "Project API"
    API_VERSION = "v1"
    API_SPEC_OPTIONS = {
        "security": [{"bearerAuth": []}],
        "components": {"securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}}},
    }
    OPENAPI_VERSION = "3.1.1"
    OPENAPI_URL_PREFIX: str | None = "/docs"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
