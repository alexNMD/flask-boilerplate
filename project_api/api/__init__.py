"""APIs"""

from flask_smorest import Api

from project_api.api.auth import auth_bp
from project_api.api.user import user_bp


def register_routes(api: Api) -> None:
    api.register_blueprint(auth_bp)
    api.register_blueprint(user_bp)
