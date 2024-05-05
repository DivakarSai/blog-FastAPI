from fastapi import APIRouter, Depends, HTTPException
from models.blog import Blog
from models.user import User
from dependencies import authenticate_user
from database import db

blog_router = APIRouter()

# Route to create a new blog
@blog_router.post("/")
async def create_blog(blog: Blog, current_user: User = Depends(authenticate_user)):
    try:
        # Add logic to insert the blog into the database
        blog_dict = blog.model_dump()
        blog_dict["author"] = current_user.username
        blogs_collection = db["blogs"]
        result = blogs_collection.insert_one(blog_dict)
        return {"message": "Blog created successfully", "blog_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Route to get all blogs with pagination
@blog_router.get("/")
async def get_all_blogs(page: int = 1, limit: int = 10):
    try:
        # Add logic to fetch blogs from the database with pagination
        skip = (page - 1) * limit
        blogs = list(db.blogs.find().skip(skip).limit(limit))
        return {"blogs": blogs}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Route to get a blog by its ID
@blog_router.get("/{blog_id}")
async def get_blog_by_id(blog_id: str):
    try:
        # Add logic to fetch a blog by its ID from the database
        blog = db.blogs.find_one({"_id": blog_id})
        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        return {"blog": blog}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Route to update a blog
@blog_router.put("/{blog_id}")
async def update_blog(blog_id: str, blog: Blog, current_user: User = Depends(authenticate_user)):
    try:
        # Add logic to update the blog in the database
        db.blogs.update_one({"_id": blog_id}, {"$set": blog.dict()})
        return {"message": "Blog updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Route to delete a blog
@blog_router.delete("/{blog_id}")
async def delete_blog(blog_id: str, current_user: User = Depends(authenticate_user)):
    try:
        # Add logic to delete the blog from the database
        db.blogs.delete_one({"_id": blog_id})
        return {"message": "Blog deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

