from flask.views import MethodView
from flask_smorest import Blueprint

from project_api.api.schema.user import UserSchema
from project_api.service.user import UserService
from project_api.helper.error_handler import with_error_responses
from project_api.service.auth import AuthService

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("")
@with_error_responses()
class User(MethodView):
    @user_bp.response(200, UserSchema(many=True))
    def get(self):
        return UserService.get_all()
