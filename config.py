import os

basedir= os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://tweep_api:tweep_api@localhost:5432/tweep_api"