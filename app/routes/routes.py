from app.main import app


@app.get("/users")
async def get_users():
    pass


@app.get("/users/id")
async def get_users_id():
    pass


@app.post("/users")
async def post_users():
    pass


@app.post("/users/login")
async def users_login():
    pass


@app.post("/users/logout")
async def users_logout():
    pass
