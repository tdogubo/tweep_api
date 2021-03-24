from flask import Blueprint, request,abort
from flask_restful import Resource
from models import db,Tweet,TweetSchema
from tweets import tweets_api

likes_blueprint = Blueprint('likes',__name__)

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)

class Likes(Resource):
    def get(self,tweet_id):
        tweet = Tweet.query.filter_by(id= tweet_id).first()
        likes= Tweet.query.filter_by(Tweet.likes)
        # likes = tweets_schema.dump(likes)
        likes = likes.count()
        return {'tweet':tweet,'likes: ': likes}
    
    def post(self,tweet_id):
        json_data = request.get_json(force= True)
        if not request.is_json:
            return {'message': 'invalid input'}
        like = json_data['user_id']

        tweet= Tweet.query.filter_by(id=tweet_id).first()
        if tweet:
            if like:
                return {'message':'tweet already liked'}, 200
            likes= Tweet(likes= like)
            db.session.add(like)
            db.session.commit()

            result=tweet_schema.dump(likes)
            return result, 200


tweets_api.add_resource(Likes,'/tweet/<string:tweet_id>')