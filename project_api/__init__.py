from typing import cast

from dotenv import load_dotenv
from flask import Flask
from flask.app import App
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from werkzeug.exceptions import HTTPException

from project_api.api import register_routes
from project_api.helper.auth import set_auth
from project_api.helper.config import load_app_config, set_commit_or_rollback
from project_api.helper.encoder import CustomJSONProvider
from project_api.helper.error_handler import json_error_handler
from project_api.helper.extension import bcrypt, db

load_dotenv()


def create_app() -> Flask:
    flask_app = Flask(__name__)

    load_app_config(flask_app)

    CORS(flask_app)

    bcrypt.init_app(flask_app)

    set_auth(flask_app)

    # OpenAPI documentation
    flask_api = Api(flask_app)
    register_routes(flask_api)

    JWTManager(flask_app)

    flask_app.json_provider_class = CustomJSONProvider
    flask_app.json = flask_app.json_provider_class(cast(App, flask_app))
    flask_app.register_error_handler(HTTPException, json_error_handler)

    db.init_app(flask_app)
    set_commit_or_rollback(flask_app)

    return flask_app
