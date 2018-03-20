import jwt
import datetime
from flask import current_app
import functools

class User():

    def __init__(self, email, password, activated,*created_at):
        self.email = email
        self.password = password
        self.created_at =  datetime.datetime.utcnow()
        self.activated = activated


    def json(self):
        return {'email':self.email,'password':self.password,'created_at':self.created_at,'activated':self.activated}

    @classmethod
    def generate_token(self, user_id):
        print('Inside gen token: ', current_app.config['SECRET_KEY'])
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    
            