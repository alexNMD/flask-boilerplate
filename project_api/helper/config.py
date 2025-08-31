import logging
import os

from flask import Flask, Response
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from project_api.helper.error_handler import json_error_handler
from project_api.helper.extension import db


def load_app_config(app: Flask) -> None:
    config_name = os.getenv("ENV_CONFIG")
    if not config_name:
        raise Exception("Environment variable 'ENV_CONFIG' not set !")

    config_path = f"project_api.config.{config_name}.Config"

    app.config.from_object(config_path)

    # Override config if needed
    app.config.update(os.environ)


def set_logger(logger: logging.Logger, app: Flask) -> None:
    app.logger.handlers = logger.handlers
    app.logger.setLevel(logger.level)
    app.logger.propagate = True
    app.logger.info("Logger configured: %s", logger.name)


def set_commit_or_rollback(app: Flask) -> None:
    @app.after_request
    def commit(response: Response) -> Response:
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError, Exception) as e:
            db.session.rollback()
            return json_error_handler(e)
        return response

    @app.teardown_appcontext
    def cleanup(exception: BaseException | None = None) -> None:
        if exception:
            db.session.rollback()
        db.session.remove()
