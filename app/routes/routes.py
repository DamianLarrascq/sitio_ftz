from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.requests import Request
from app.controllers import crud
from app.models import schemas
from app.models.base import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


users_router = APIRouter(
    # prefix="/items",
    tags=["users"],
    dependencies=[Depends(oauth2_scheme)],
    # responses={404: {"description": "Not found"}},
)
auth_router = APIRouter(
    # prefix="/items",
    tags=["auth"],
    # dependencies=[Depends(oauth2_scheme)],
    # responses={404: {"description": "Not found"}},
)


@auth_router.post("/token")
async def get_token(request: Request, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(form_data)
    return form_data


@users_router.get("/users/", response_model=list[schemas.UserGet])
async def get_users(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@users_router.get("/users/{user_id}")
async def get_users_id(request: Request, user_id: int, token=Depends(oauth2_scheme)):
    return user_id


@users_router.post("/users", response_model=schemas.UserCreateResponse)
async def post_users(request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    result = crud.create_user(db, user.email, user.password)

    return result

