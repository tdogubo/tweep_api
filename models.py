from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import FetchedValue
from uuid import uuid4

ma = Marshmallow()
db = SQLAlchemy()

class Likes(db.Model):
    __tablename__= 'likes'
    tweet_id =db.Column(UUID(as_uuid=True), db.ForeignKey('tweets.id', ondelete='CASCADE'),primary_key=True, nullable=False, default = lambda: uuid4().hex,unique = False)
    likes =db.Column(UUID(as_uuid=True), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, default = lambda: uuid4().hex)
    creation_date = db.Column(db.TIMESTAMP, server_default= db.func.now(), nullable = False)
    user = db.relationship('User', backref= db.backref('likes', lazy='dynamic'))
    tweets = db.relationship('Tweet', backref= db.backref('likes', lazy='dynamic'))


    def __init__(self,tweet_id,likes):
        self.likes= likes
        self.tweet_id= tweet_id

class Tweet(db.Model):
    __tablename__= 'tweets'
    id = db.Column(UUID(as_uuid=True), primary_key = True,default = lambda: uuid4().hex)
    tweet = db.Column(db.String(500), nullable = False)
    creation_date = db.Column(db.TIMESTAMP, server_default= db.func.now(), nullable = False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, default = lambda: uuid4().hex)
    user = db.relationship('User', backref= db.backref('tweets', lazy='dynamic'))

    def __init__(self,tweet,user_id):
        self.tweet= tweet
        self.user_id= user_id

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key = True,default = lambda: uuid4().hex)
    first_name = db.Column(db.String(150),nullable= False)
    last_name = db.Column(db.String(150),nullable= False)
    username = db.Column(db.String(100),unique=True,nullable= False)
    password = db.Column(db.String(100),unique=True,nullable= False)
    email = db.Column(db.String(150),unique=True,nullable= False)
    phone_number = db.Column(db.String(14),nullable= False)

    def __init__(self,username,first_name,last_name,password,email,phone_number):
        self.username=username
        self.first_name=first_name
        self.last_name =last_name 
        self.password=password
        self.email=email
        self.phone_number= phone_number

    


class UserSchema(ma.Schema):
    id= fields.UUID(as_uuid=True)
    username= fields.String(required= True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.String(required=True)

class TweetSchema(ma.Schema):
    id= fields.UUID(as_uuid=True)
    user_id=fields.UUID(required= True)
    tweet= fields.String(required=True)
    creation_date = fields.DateTime()

class LikesSchema(ma.Schema):
    tweet_id= fields.UUID(required=True,unique=False)
    likes=fields.UUID(required= True)
    creation_date = fields.DateTime()
