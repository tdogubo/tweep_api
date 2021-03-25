from flask import Blueprint, request,abort
from flask_restful import Resource
from models import db,Likes,LikesSchema
from tweets import tweets_api

likes_blueprint = Blueprint('likes',__name__)

like_schema = LikesSchema()
likes_schema = LikesSchema(many=True)


class Like(Resource):
    def get(self,tweet_id):
        tweet = Likes.query.filter_by(tweet_id=tweet_id)
        tweet = likes_schema.dump(tweet)
        count = len(tweet)
        return {'tweet':tweet,'likes: ':count}
    
    def post(self,tweet_id):
        json_data = request.get_json(force= True)
        if not request.is_json:
            return {'message': 'invalid input'}
        user_tweet= json_data['tweet_id']
        like = json_data['user_id']

        tweet= Likes.query.filter_by(tweet_id=tweet_id).first()
        like= Likes.query.filter_by(likes=like).first()

        if tweet and like:
            return {'message':'tweet already liked'}, 200
            
        likes= Likes(likes= like,tweet_id=user_tweet)
        db.session.add(likes)
        db.session.commit()

        result=like_schema.dump(likes)
        return result, 200


tweets_api.add_resource(Like,'/tweet/<string:tweet_id>')