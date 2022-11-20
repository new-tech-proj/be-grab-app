from app import app

from app.dtos import dtoUser, dtoUserLogin, dtoPost
from app.models import User, Post
from app.database import session
from app.utils import verify_password, make_respones, is_exists_user, get_hash_password
from app.services import insert_post, insert_user

@app.get("/")
def index():
    return make_respones(
        status_code=0,
        message="Welcome to server of grab application",
        data=dict()
    )

@app.post("/signup")
def sign_up(user_data: dtoUser):
    if is_exists_user(user_data.username):
        message = "username already exists!"
        return make_respones(status_code=0, message=message)
    
    user_data = dict(user_data)
    user_data['hashed_password'] = get_hash_password(user_data['hashed_password'])
    user = User(**user_data)

    data = insert_user(session, user)
    if data is not None:
        return make_respones(
            status_code=0,
            message="Created user successful",
            data=data
        )

    return make_respones(message="Error when create new user")

@app.post("/login")
def login(form_data: dtoUserLogin):
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


@app.post("/user/post")
def create_post(post_data: dtoPost):
    post = Post(**dict(post_data))
    data = insert_post(session, post)
    if data is not None:
        return make_respones(
            status_code=0,
            message="Created post successful",
            data=data
        )
    
    return make_respones(message="Error when insert new post")