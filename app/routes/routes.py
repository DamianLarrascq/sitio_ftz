from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from app.controllers import crud
# from app.main import oauth2_scheme
from app.models import schemas
from app.models.base import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


users_router = APIRouter(
    # prefix="/items",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


# @users_router.get("/users/getuser")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}


@users_router.get("/users/", response_model=list[schemas.UserGet])
async def get_users(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@users_router.get("/users/{user_id}")
async def get_users_id(request: Request, user_id: int):
    return user_id


@users_router.post("/users", response_model=schemas.UserCreateResponse)
async def post_users(request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    result = crud.create_user(db, user.email, user.password)

    return result


@users_router.post("/users/login")
async def users_login():
    pass


@users_router.post("/users/logout")
async def users_logout():
    pass
