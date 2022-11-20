from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app import app
from fastapi import Response

from app.dtos import dtoUser

from app.models import User
from app.database import session
from app.utils import verify_password, make_respones, is_exists_user, insert_user

@app.post("/signup")
def sign_up(user: dtoUser):
    if is_exists_user(user.username):
        message = "username already exists!"
        return make_respones(status_code=0, message=message)
    message = insert_user(dict(user))
    return make_respones(status_code=1, message=message)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    user = session.query(User).filter(User.username == username).first()
    
    if user is not None:
        if verify_password(password, user.hashed_password):
            return make_respones(
                status_code=0,
                message="Login successful",
                data={
                    "user_id": user.id
                }
            )
    else:
        return make_respones(message="Wrong username or password")


@app.get("/user/posts")
def get_post_by_user(user_id: int):
    author_id = user_id
    posts = session.query(Post).filter(Post.author_id == author_id).all()
    if posts != []:
        return make_respones(
            status_code=0,
            message=f"Get all posts of user {author_id} successful",
            data=posts
        )
    
    return make_respones(message=f"Failure to get all posts of user {author_id}")