import jwt
import datetime
from flask import current_app
import functools
from mongoengine import *

class User(Document):

    email = StringField(required=True, max_length=30)
    password = StringField(required=True, max_length=100)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    activated = BooleanField(default=False)
    token = StringField(default="")

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
    
    
            