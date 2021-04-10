from flask import Blueprint, request,abort
from flask_restful import Resource, Api
from models import db, User,UserSchema
from werkzeug.security import generate_password_hash


user_blueprint = Blueprint('user',__name__)
user_api = Api(user_blueprint)

user_schema = UserSchema()
users_schema = UserSchema(many=True)



class Profile(Resource):
    def post(self,user_id):
        user = User.query.get(user_id)
        result = user_schema.dump(user)

        if not user:
            return {'message':'User not found'},404

        return {'message':'Welcome '+ user.username,'data':result},200


    def put(self,user_id):
        json_data = request.get_json(force= True)
        user = User.query.get(user_id)
        result = user_schema.dump(user)
        if not user:
            return abort(404, message='Invalid User id')
        if json_data['phone_number']:
            user.phone_number = json_data['phone_number']

        if json_data['password']:
            user.password = generate_password_hash(json_data['password'])

        if json_data['email']:
            user.password = json_data['email']

        db.session.commit()

        return result



user_api.add_resource( Profile,'/user/profile/<string:user_id>')

