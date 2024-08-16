
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.models.base import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = Column(String)
    last_name: Mapped[str] = Column(String)

