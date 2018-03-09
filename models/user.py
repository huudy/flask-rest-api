import sqlite3
from flask_restful import Resource, reqparse
from db import db
import datetime


class User(db.Model):
    TABLE_NAME = 'users'
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    created_at = db.Column(db.Date)
    activated = db.Column(db.Boolean)

    reservations = db.relationship('ItemModel', lazy='dynamic')



    def __init__(self, email, password, created_at, activated):
        self.email = email
        self.password = password
        self.created_at = created_at
        self.activated = activated

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  