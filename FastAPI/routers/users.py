from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

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
@router.get("/users")
async def users():
    return users_list


# Get 1 user by path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Get 1 user by query parameter
@router.get("/userquery/")
async def userquery(id: int):
    return search_user(id)


@router.post("/user/new", response_model=User, status_code=201)
async def usernew(user: User):
    return add_user(user)


@router.put("/user/update", status_code=201)
async def userupdate(user: User):
    return update_user(user)


@router.delete("/user/delete/{id}")
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
    return user 


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
