from werkzeug.security import safe_str_cmp
from models.user import User
from mongo import db
from werkzeug.security import check_password_hash


def authenticate(email, password):
    user = db.users.find_one({'email':email})
    print(user)
    if user and check_password_hash(user['password'], password):
        print('Returnig user in authenticate')
        return user

def identity(payload):
    print('Payload: ',payload)
    user_id = payload['_id']
    return {"user_id": user_id}