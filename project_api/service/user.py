from sqlalchemy import select

from project_api.helper.extension import db
from project_api.model.user import User


class UserService:
    @classmethod
    def get_all(cls):
        return db.session.scalars(select(User)).all()
