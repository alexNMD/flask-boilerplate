
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from project_api.helper.extension import Base


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    password: Mapped[str]
