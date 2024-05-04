

from fastapi import FastAPI

app = FastAPI()

from routes.auth import auth_router

app.include_router(prefix="", router=auth_router, tags=["Authentications"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
