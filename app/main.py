from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import auth_router
from routes.blog import blog_router

app = FastAPI()

origins = ["http://localhost:3000", "http://localhost", "http://localhost:5000"]


app.include_router(prefix="/users", router=auth_router, tags=["Authentications"])
app.include_router(prefix="/blogs", router=blog_router, tags=["Blogs"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def get_root():
    return { "Ping": "Pong" }


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
