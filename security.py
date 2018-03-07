from werkzeug.security import safe_str_cmp
from models.user import User

def authenticate(email, password):
    user = User.find_by_email(email)
    if user and safe_str_cmp(user.password, password):
        print('Returnig user in authenticate')
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)