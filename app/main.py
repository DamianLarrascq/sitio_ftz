from fastapi import FastAPI
from app.routes.routes import users_router
import uvicorn
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

app.include_router(users_router)

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@users_router.get("/")
def get_home():
    return {'message': 'algo'}


uvicorn.run(app, host="127.0.0.1", port=8000)
