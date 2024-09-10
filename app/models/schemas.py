from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserCreateResponse(UserBase):
    pass


class UserGet(UserBase):
    id: int | None
    first_name: str | None
    last_name: str | None
    dni: int | None
    phone_number: str | None

    class Config:
        orm_mode = True


class UserLogin(UserCreate):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
