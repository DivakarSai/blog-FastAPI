import uvicorn # ASGI server

from fastapi import FastAPI

from database import database

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=8080, reload=True)

