from fastapi import FastAPI
from services.user import UserService

app = FastAPI()
userService = UserService()

@app.get("/users")
def get_users(page = 1, limit = 10):
    users = userService.get_users(int(page), int(limit))
    return {"ok": True, "users": users}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = userService.get_user(user_id);

    if not user:
        return { 'ok': False, 'message': 'user not found', }

    return { 'ok': True, "user": user}


@app.post("/users")
def create_user():
    pass


@app.patch("/users/{user_id}")
def update_user():
    pass

@app.delete("/users/{user_id}")
def delete_user():
    pass