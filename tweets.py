from flask import Blueprint, request,abort
from flask_restful import Resource, Api
from models import db,Tweet,TweetSchema

tweet_blueprint = Blueprint('tweets',__name__)
tweets_api = Api(tweet_blueprint)

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)


class Tweets(Resource):
    def get(self):
        tweets = Tweets.query.all()
        tweets = tweets_schema.dump(tweets)
        return {'status':'success','data':tweets}, 200


class Tweet(Resource):
    def get(self,tweet_id):
        json_data = request.get_json(force= True)
        if not json_data:
            return {'message':'No input data provided'}

        first_name = json_data['first_name']
        last_name = json_data['last_name']
        username = json_data['username']
        email = json_data['email']
        password = json_data['password']
        phone_number = json_data['phone_number']
        tweet = Tweets.query.filter_by(id=tweet_id).first()
