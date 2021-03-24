from flask import Blueprint, request,abort
from flask_restful import Resource, Api
from models import db,Tweet,TweetSchema

tweet_blueprint = Blueprint('tweets',__name__)
tweets_api = Api(tweet_blueprint)

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)


class AllUserTweets(Resource):
    def get(self,user_id):
        tweets = Tweet.query.filter_by(user_id=user_id)
        tweets = tweets_schema.dump(tweets)
        return {'tweets':tweets}, 200

    
class NewTweet(Resource):
    def post(self):
        json_data = request.get_json(force= True)
        if not request.is_json:
            return {'message':'Invalid request'}
        new_tweet = json_data['tweet']
        user_id = json_data['user_id']

        tweet = Tweet.query.filter_by(tweet=new_tweet).first()
        if tweet:
            return {'message':'tweet already exists'},409
        tweet= Tweet(tweet= new_tweet,
        user_id= user_id)

        db.session.add(tweet)
        db.session.commit()
        result = tweet_schema.dump(tweet)

        return {'status':'created','data': result},201
        

class UserTweet(Resource):
    def post(self,tweet_id):
        tweet = Tweet.query.get(tweet_id)
        result = tweet_schema.dump(tweet)

        if not tweet:
            return {'status':'Not Found'},404

        return {'status':'success','data':result},200
    
    def delete(self,tweet_id):
        tweet = Tweet.query.filter_by(id=tweet_id).first()
        all_tweets = Tweet.query.all()
        all_tweets= tweets_schema.dump(all_tweets)
        if not request.is_json:
            abort(400, "invalid format for tweet")
        if not tweet:
            abort(400, "Tweet not found")
        db.session.delete(tweet)
        db.session.commit()
        return {'status':'sucessfully deleted','data':all_tweets}        


tweets_api.add_resource(AllUserTweets,'/user/<string:user_id>/tweets')
tweets_api.add_resource(NewTweet,'/user/profile/new_tweet')
tweets_api.add_resource(UserTweet,'/user/profile/tweet/<string:tweet_id>')


