import jwt
import functools
from werkzeug.security import safe_str_cmp
from models.user import User
from mongo import db
from flask import request, current_app
from werkzeug.security import check_password_hash



def authenticate(email, password):
    user = db.users.find_one({'email':email})
    if user and check_password_hash(user['password'], password):
        
        result = User(**user)
        print('Returnig user in authenticate: ', result)
        return result

def identity(payload):
    print('Payload: ',payload)
    user_id = payload['_id']
    user = db.users.find_one({'_id':user_id})
    print(user)
    return user

def login_required(func):
        @functools.wraps(func)
        def check_token(self,name):
            token = request.headers.get('Authorization')
            print('HEad:',token)
            
            if token:
                try:
                    payload = jwt.decode(token, current_app.config['SECRET_KEY'] ,algorithms=['HS256'])
                    print('Payload: ', payload)
                    #return payload['sub']
                    
                except jwt.ExpiredSignatureError:
                    return 'Signature expired. Please log in again.'
                except jwt.InvalidTokenError:
                    return 'Invalid token. Please log in again.'

                func(self,name)
            else:
                 return {'message':'You have to be logged in to perform this action!'}   
        return check_token