from flask import Flask
from flask_restful import Api
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.database_crud import *


flask_back = Flask(__name__)
api = Api(flask_back)
api.add_resource(RestApi, '/share-api', '/share-api/', '/share-api/<string:id>', '/share-api/<int:id>')
flask_back.config.from_object(Config)
db = SQLAlchemy(flask_back)
migrate = Migrate(flask_back, db)

from app.models import *

