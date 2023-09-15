from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Entidad user
class User(BaseModel):
    id: int
    name: str
    age: int
    url: str


users_list = [
    User(id=1, name="John", age=30, url="https://google.com"),
    User(id=2, name="Jane", age=25, url="https://moure.dev"),
    User(id=3, name="Jack", age=27, url="https://youtube.com"),
]


# Get all users
@app.get("/users")
async def users():
    return users_list


# Get 1 user
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="User not found")
