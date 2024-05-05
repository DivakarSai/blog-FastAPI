

from fastapi import FastAPI

app = FastAPI()

from routes.auth import auth_router
from routes.blog import blog_router

app.include_router(prefix="", router=auth_router, tags=["Authentications"])
app.include_router(prefix="/blogs", router=blog_router, tags=["Blogs"])


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
