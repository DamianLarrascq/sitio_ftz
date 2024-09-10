import bcrypt
from sqlalchemy.orm import Session

from app.models import models


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[type(models.User)]:
    result = db.query(models.User).offset(skip).limit(limit).all()

    return result


def get_user_by_email(db: Session, email: str) -> models.User:
    result = db.query(models.User).filter(models.User.email == email).first()

    return result


def get_user_by_id(db: Session, user_id: int):
    result = db.query(models.User).filter(models.User.id == user_id).fist()


def create_user(db: Session, email: str, password: str):
    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password.encode(), salt)
    db_user = models.User(email=email, password_hash=hashed.decode())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
