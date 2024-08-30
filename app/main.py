from fastapi import FastAPI
from app.routes.routes import users_router, auth_router
import uvicorn

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)


@users_router.get("/")
def get_home():
    return {'message': 'algo'}


uvicorn.run(app, host="127.0.0.1", port=8001)
