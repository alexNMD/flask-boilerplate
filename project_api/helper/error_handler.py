from collections.abc import Callable
from typing import Any, TypeVar

from flask import Response
from flask_smorest import Blueprint
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import HTTPException, UnprocessableEntity

from project_api.api.schema.response import ErrorResponseSchema
from project_api.helper.response_factory import response_error

T = TypeVar("T")


def json_error_handler(error: Exception) -> Response:
    match error:
        case UnprocessableEntity():
            data: str | dict[str, Any] | None = error.description
            if hasattr(error, "data"):
                data_exception = error.data.get("messages", {})
                data = {**data_exception.get("json", {}), **data_exception.get("query", {})}
            return response_error(message=error.name, data=data, http_code=error.code)
        case HTTPException():
            return response_error(message=error.name, data=error.description, http_code=error.code)
        case IntegrityError():
            return response_error(message=str(error.orig), http_code=400)
        case DatabaseError():
            return response_error(message=str(error.orig))
        case _:
            return response_error(message="Internal Server Error")


def with_error_responses() -> Callable[[type[T]], type[T]]:
    def decorator(cls: type[T]) -> type[T]:
        error_doc = {
            "default": {
                "description": "Default error response",
                "content": {"application/json": {"schema": ErrorResponseSchema}},
            }
        }

        for method_name in ["get", "post", "put", "delete", "patch"]:
            if hasattr(cls, method_name):
                method = getattr(cls, method_name)
                decorated_method = Blueprint.doc(responses=error_doc)(method)
                setattr(cls, method_name, decorated_method)

        return cls

    return decorator
