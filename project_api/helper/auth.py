from typing import TypeVar

from flask import Flask, request
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended.exceptions import JWTExtendedException
from werkzeug.exceptions import Unauthorized

T = TypeVar("T")


def no_jwt_needed_class(cls: type[T]) -> type[T]:
    cls._auth_exempt = True
    return cls


def set_auth(app: Flask) -> None:
    @app.before_request
    def require_jwt() -> None:
        endpoint = request.endpoint
        if not endpoint:
            return None

        if request.blueprint == "api-docs":
            return None

        view_func = app.view_functions.get(endpoint)
        if hasattr(view_func, "view_class") and getattr(view_func.view_class, "_auth_exempt", False):
            return None

        try:
            if not verify_jwt_in_request():
                return None
        except JWTExtendedException as auth_error:
            raise Unauthorized from auth_error
