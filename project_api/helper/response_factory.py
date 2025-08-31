from typing import Any

from flask import Response, jsonify, make_response


def response_ok(data: Any | None = None, message: str = "Success") -> Response:
    return make_response(
        jsonify(
            {
                "status": "success",
                "message": message,
                "data": data,
            }
        ),
        200,
    )


def response_created(data: Any | None = None, message: str = "Resource created") -> Response:
    return make_response(
        jsonify(
            {
                "status": "success",
                "message": message,
                "data": data,
            }
        ),
        201,
    )


def response_error(message: str | None, data: Any = None, http_code: int | None = 500) -> Response:
    return make_response(jsonify({"status": "error", "message": message, "data": data}), http_code)
