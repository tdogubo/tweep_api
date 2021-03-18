from flask import Flask
from flask_restful import Api

api= Api()
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    api.init_app(app)
    
    from user import user_blueprint
    app.register_blueprint(user_blueprint)

    from tweets import tweet_blueprint
    app.register_blueprint(tweet_blueprint)

    from auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from models import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)