from app import app 
from mongoengine import *
connect('FlaskMongo', host=os.environ.get('MONGODB_URI', None))
