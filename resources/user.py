import datetime
import sendgrid
import os
from sendgrid.helpers.mail import *
from flask import request, current_app, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from models.user import User
from bson.json_util import dumps
from itsdangerous import URLSafeTimedSerializer

class UserRegister(Resource):

    def post(self):
        data = request.get_json()
        userInDB = User.objects(email=data['email'])
        if userInDB:
            return {"message": "User with that username already exists."}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')       
        token = User.generate_confirmation_token(data['email'])

        confirm_url = url_for('confirmemail', token=token, _external=True)

        sg = sendgrid.SendGridAPIClient(apikey=current_app.config['SENDGRID_KEY'])
        from_email = Email("office@agrohouse.pl")
        to_email = Email(data['email'])
        subject = "Welcome to AgroHouse"
        content = Content("text/html", """<p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p>
                                        <p><a href="{0}">{0}</a></p>
                                        <br>
                                        <p>Cheers!</p>""".format(confirm_url))
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

        user = User(data['email'], hashed_password)

        user.save()

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):

    def post(self):
        data = request.get_json()
        user = User.objects.get(email=data['email'])
        print('ID: ',user.id)
        if user and check_password_hash(user.password, data['password']):
            token = User.generate_token(str(user.id))
            User.objects(email=data['email']).update_one(set__token = token.decode())
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'token': token.decode()
            }
            return responseObject, 201
        return {'message':'Wrong user/password combination. Please verify!'}

class UserLogout(Resource):
    def post(self):
        pass

class ConfirmEmail(Resource):
    def get(self, token):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:  
            email = serializer.loads(
                token,
                salt=current_app.config['SECURITY_PASSWORD_SALT'],
                max_age=3600
            )
        except:
            return {"message": "An error occurred loading token."}

        user = User.objects.get(email=email)
        user.activated = True
        user.save()
        
        return {'message':'Account activated'}
