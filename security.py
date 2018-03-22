import jwt
import functools
from werkzeug.security import safe_str_cmp
from models.user import User
from flask import request, current_app
from werkzeug.security import check_password_hash

def login_required(func):
        @functools.wraps(func)
        def check_token(self,*name):
            token = request.headers.get('Authorization')
            print('HEad:',token)
            
            if token:
                try:
                    payload = jwt.decode(token, current_app.config['SECRET_KEY'] ,algorithms=['HS256'])                    
                except jwt.ExpiredSignatureError:
                    return 'Signature expired. Please log in again.'
                except jwt.InvalidTokenError:
                    return 'Invalid token. Please log in again.'

                func(self,name)
            else:
                 return {'message':'You have to be logged in to perform this action!'}   
        return check_token