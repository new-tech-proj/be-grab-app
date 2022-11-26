from app import app
from app import success_status, fail_status
from app.dtos import *
from app.models import User, Post
from app.database import session
from app.utils import verify_password, make_respones, is_exists_user, get_hash_password
from app.services import insert_post, insert_user

from datetime import datetime

@app.get("/")
def index():
    return make_respones(
        status_code=0,
        message="Welcome to server of grab application",
        data=dict()
    )
    
@app.put("/edit_post")
def edit_post(post_id: int, new_post: dtoUpdatePost):
    post = session.query(Post).filter(Post.id == post_id)
    if post.fetchall():
        try:
            new_post = dict(new_post)
            new_post['last_modified_date'] = datetime.now()
            post.update(new_post)
            session.commit()
        except Exception as e:
            raise SystemExit(e)
    else:
        make_respones(status_code=fail_status, message="Post does not exists!")
    return make_respones(status_code=success_status, message="Update post successful!")


@app.delete("/delete_post")
def delete_post(post_id: int):
    post = session.query(Post).filter(Post.id == post_id)
    if not post.fetchall():
        return make_respones(status_code=fail_status, message="Post not found!")
    post.delete()
    session.commit()
    return make_respones(status_code=success_status, message="Delete post successful!")
        
    
@app.get("/post")
def get_post_by_id(post_id: int):
    if type(post_id) != int:
        return make_respones(
            status_code=fail_status,
            message="Invalid data type of post_id!"
        )
    
    query = f"select * from posts where id = {post_id}"
    post = session.execute(query).fetchall()
    
    if not post:
        return make_respones(
            status_code=fail_status,
            message=f"Do not exists {post_id} post!"
        )
    else:
        keys = post[0].keys()
        data = {k: v for k, v in zip(keys, post[0])}
        return make_respones(
                status_code=success_status,
                message="Successfully!",
                data=data
        )
        
@app.post("/signup")
def sign_up(user_data: dtoUser):
    if is_exists_user(user_data.username):
        message = "username already exists!"
        return make_respones(status_code=fail_status, message=message)
    
    user_data = dict(user_data)
    user_data['hashed_password'] = get_hash_password(user_data['hashed_password'])
    user = User(**user_data)

    data = insert_user(session, user)
    if data is not None:
        return make_respones(
            status_code=success_status,
            message="Created user successful",
            data=data
        )

    return make_respones(status_code=fail_status, message="Error when create new user")

@app.post("/login")
def login(form_data: dtoUserLogin):
    username = form_data.username
    password = form_data.password

    user = session.query(User).filter(User.username == username).first()
    
    if user is not None:
        if verify_password(password, user.hashed_password):
            return make_respones(
                status_code=success_status,
                message="Login successful",
                data={
                    "user_id": user.id
                }
            )
    
    return make_respones(status_code=fail_status, message="Wrong username or password")


@app.get("/user/posts")
def get_post_by_user(user_id: int):
    author_id = user_id
    posts = session.query(Post).filter(Post.author_id == author_id).all()
    if posts != []:
        return make_respones(
            status_code=success_status,
            message=f"Get all posts of user {author_id} successful",
            data=posts
        )
    
    return make_respones(status_code=fail_status, message=f"Failure to get all posts of user {author_id}")


@app.post("/user/post")
def create_post(post_data: dtoPost):
    post = Post(**dict(post_data))
    data = insert_post(session, post)
    if data is not None:
        return make_respones(
            status_code=success_status,
            message="Created post successful",
            data=data
        )
    
    return make_respones(message="Error when insert new post")


@app.get("/search")
def search_posts(query: str):
    data = session.query(Post) \
        .filter(Post.title.contains(query) | Post.desc.contains(query)) \
        .all()
    if data is not None and data != []:
        return make_respones(
            status_code=success_status,
            message="Get all post by search query successful",
            data=data
        )
    
    return make_respones(message="No posts match search query")