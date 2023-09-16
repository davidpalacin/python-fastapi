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


# Get 1 user by path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Get 1 user by query parameter
@app.get("/userquery/")
async def userquery(id: int):
    return search_user(id)


@app.post("/user/new")
async def usernew(user: User):
    return add_user(user)


@app.put("/user/update")
async def userupdate(user: User):
    return update_user(user)


@app.delete("/user/delete/{id}")
async def userdelete(id: int):
    return delete_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "error": "User not found" }

def add_user(user: User):
    user_exist = search_user(user.id)
    if type(user_exist) == User:
        return { "error": "El usuario ya existe." }
    users_list.append(user)
    return { "message": "user created", "user": user }  


def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return { "message": "User updated.", "user": user }
    return { "error": "User not found." }


def delete_user(id: int):
    for index, user in enumerate(users_list):
        if user.id == id:
            del users_list[index]
            return { "message": "Deleted", "list": users_list }
    return {"error": "User not found."}
