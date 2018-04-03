import jwt
import functools
from werkzeug.security import safe_str_cmp
from models.user import User
from flask import request, current_app
from werkzeug.security import check_password_hash

def login_required(func):
        @functools.wraps(func)
        def check_token(self,*user_id):
            token = request.headers.get('Authorization')            
            if 'Bearer' in str(token):
                try:
                    token = token.split(' ')[1]
                    payload = jwt.decode(token, current_app.config['SECRET_KEY'] ,algorithms=['HS256']) 
                    user_id = payload['sub']
                except jwt.ExpiredSignatureError:
                    return 'Signature expired. Please log in again.', 400
                except jwt.InvalidTokenError:
                    return 'Invalid token. Please log in again.', 400
                func(self,user_id)
            else:
                 return {'message':'You have to be logged in to perform this action!'}, 401   
        return check_token