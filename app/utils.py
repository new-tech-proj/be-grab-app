from passlib.context import CryptContext
from app.database import session


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
    
def is_exists_user(username: str, phone_number: str):
    query = f"select * from users where username = '{username}' or phone_number = '{phone_number}'"
    result = session.execute(query).fetchall()
    if result:
        return True
    return False

def sms_auth(phone_number: str):
    from twilio.rest import Client
    import random
    random_token = random.randrange(123456, 987654, 1)
    account_sid = "AC162565ee2c928192c270d346cbcfd066"
    auth_token  = "40673c6b3866be65a9959606e4a2cbd3"
    
    client = Client(account_sid, auth_token)
    phone_number = '+84' + phone_number[1:]
    message = client.messages.create(
        to=phone_number,
        from_="+15625739883",
        body=random_token)
        # body=str(random_token))
    message.sid
    return random_token
    