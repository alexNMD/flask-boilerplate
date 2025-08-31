from datetime import timedelta

from flask_jwt_extended import create_access_token
from sqlalchemy import select
from werkzeug.exceptions import Unauthorized

from project_api.helper.extension import bcrypt, db
from project_api.model.user import User


class AuthService:
    @classmethod
    def generate_jwt_token(cls, whoami: dict) -> str:
        return create_access_token(
            identity=str(whoami["id"]), expires_delta=timedelta(hours=12), additional_claims=whoami
        )

    @classmethod
    def authenticate_user(cls, name: str, password: str) -> str:
        user = db.session.scalars(select(User).where(User.name == name)).one()
        if not bcrypt.check_password_hash(user.password, password):
            raise Unauthorized()

        whoami = {"id": user.id, "name": user.name}

        return cls.generate_jwt_token(whoami)
