from passlib.context import CryptContext


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