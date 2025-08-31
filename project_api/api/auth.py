from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from project_api.api.schema.auth import AuthLoginSchema, AuthTokenSchema
from project_api.helper.auth import no_jwt_needed_class
from project_api.helper.error_handler import with_error_responses
from project_api.service.auth import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login")
@with_error_responses()
@no_jwt_needed_class
class AuthLogin(MethodView):
    @auth_bp.arguments(AuthLoginSchema, location="json")
    @auth_bp.response(200, AuthTokenSchema)
    def post(self, args: dict):
        name = args["name"]
        password = args["password"]

        return jsonify({"token": AuthService.authenticate_user(name, password)})
