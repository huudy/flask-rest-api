import jwt
import datetime
from flask import current_app
import functools
from mongoengine import *
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash
import os


class User(Document):
    
    email = EmailField(required=True, max_length=30)
    password = StringField(required=True, max_length=100)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    activated = BooleanField(default=False)
    token = StringField(default="")
    reservations = ListField()

    def set_pass(self, password):
        self.password = generate_password_hash(password)
    def json(self):
        return {'email':self.email,'password':generate_password_hash(self.password, method='sha256'),'created_at':self.created_at,'activated':self.activated}

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
    
    @classmethod
    def generate_confirmation_token(self,email):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        salt = os.environ.get('SECURITY_PASSWORD_SALT')
        return serializer.dumps(email, salt)   
                
                