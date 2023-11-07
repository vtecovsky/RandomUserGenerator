from sqlalchemy.orm import Mapped, mapped_column

from src.storage.sql.__mixin__ import IdMixin
from src.storage.sql.models import Base


class User(Base, IdMixin):
    __tablename__ = "users"
    fullname: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    address: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
