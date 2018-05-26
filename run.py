from app import app 
from mongoengine import *
import os
connect('FlaskMongo', host=os.environ.get('MONGODB_URI', None))
