from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

bcrypt = Bcrypt()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
