from fastapi import FastAPI
from routers import products, users


app = FastAPI()


# Routers
app.include_router(products.router)
app.include_router(users.router)


@app.get("/")
async def root():
  return "Hola FastAPI!"


@app.get("/msg")
async def getMsg():
  return { "message": "Hola FastAPI!" }


@app.get("/user/{id}")
async def getUser(id: int):
  return {
    "message": "Recibiendo al usuario " + str(id)
  }