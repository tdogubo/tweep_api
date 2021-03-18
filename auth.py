from flask import Blueprint,request,abort
from flask_restful import Resource, Api
from models import db, User,UserSchema
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth',__name__)

auth_api = Api(auth_blueprint)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class AllUsers(Resource):
    def get(self):
        users = User.query.all()
        if not users:
            return "empty"
        users = users_schema.dump(users)
        return {'status':'success','data':users}, 200

class Signup(Resource):
    def post(self):
        json_data = request.get_json(force= True)
        if not json_data:
            return {'message':'No input data provided'}
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        username = json_data['username']
        email = json_data['email']
        password = json_data['password']
        phone_number = json_data['phone_number']

        user= User.query.filter_by(username= username).first()
        if user:
            return {'message':'User already exists'},409
        
        new_user = User(first_name = first_name,
        last_name = last_name,
        username = username,
        email = email,
        password = generate_password_hash(password),
        phone_number = phone_number)
        
        if username is None or password is None:
            abort(400) # missing username or password
        
                
        db.session.add(new_user)
        db.session.commit()

        result = user_schema.dump(new_user)

        return {'status':'success','data': result},201

class Login(Resource):
    def post(self):
        json_data = request.get_json(force= True)
        username = json_data['username']
        password = json_data['password']

        try:
            user = User.query.filter_by(username=username).first()

            if not username or not check_password_hash(user.password, password):
                return {'message':'Invalid username or password'},404

            return {'status':'success'},200
            
        except AttributeError:
            return {'message':'Invalid username or password'},404

class DeleteAccount(Resource):
    def delete(self,user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404, "User does not exist in database.")
        db.session.delete(user)
        db.session.commit()
        return {'message':'User deleted successfully'},200




auth_api.add_resource(AllUsers,'/users')
auth_api.add_resource(Signup,'/signup')
auth_api.add_resource(Login,'/login')
auth_api.add_resource(DeleteAccount,'/user/profile/delete_account/<string:user_id>')
