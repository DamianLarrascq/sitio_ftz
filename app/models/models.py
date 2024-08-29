
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped

from app.models.base import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = Column(String)
    last_name: Mapped[str] = Column(String)
    dni: Mapped[int] = Column(Integer)
    phone_number: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    password_hash: Mapped[str] = Column(String)


class Role(Base):
    __tablename__ = 'roles'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String)


class UserInRole(Base):
    __tablename__ = 'users_in_role'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String)
    user_id: Mapped[int] = Column(ForeignKey("users.id"))
    role_id: Mapped[int] = Column(ForeignKey("roles.id"))
