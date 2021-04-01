from flask import Blueprint, request, abort
from flask_restful import Resource
from models import db,Tweet,User
from tweets import tweets_api



likes_blueprint = Blueprint('likes',__name__)


class Like(Resource):
    def get(self,tweet_id):
        x = User.query.filter(User.tweets.any(id=tweet_id)).all()
        return {'message': x}

    
    def post(self,tweet_id):
        json_data = request.get_json(force= True)
        if not request.is_json:
            return {'message': 'invalid input'}
        user_id = json_data['user_id']
        user= User.query.filter_by(id=user_id).first()
        tweet= Tweet.query.filter_by(id=tweet_id).first()

        user.tweets.append(tweet)
        db.session.add(tweet)
        db.session.commit()
        return 'done'

    def delete(self,tweet_id):
        user= db.session.query(User).get(tweet_id)

        if not user:
            abort(404, "User not found")

        db.session.delete(user)
        db.session.commit()
        return 'done'

tweets_api.add_resource(Like,'/tweet/<string:tweet_id>')