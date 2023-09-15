from fastapi import FastAPI

app = FastAPI()

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