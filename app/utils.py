from passlib.context import CryptContext
from app.database import session
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash_password(password: str):
    return pwd_context.hash(password)

def make_respones(status_code: int = 1, message: str = "Failure", data: dict = None):
    return {
        "status_code": status_code,
        "message": message,
        "data": data
    }
    
def is_exists_user(username: str):
    query = f"select * from users where username = '{username}'"
    result = session.execute(query).fetchall()
    if result:
        return True
    return False

def insert_user(user: dict):
    user['hashed_password'] = pwd_context.hash(user['hashed_password'])
    user = User(**user)
    session.add(user)
    session.commit()
    session.close()
    return "Successful insert user!"