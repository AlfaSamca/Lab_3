import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://mouz:1234@rest_db:5432/rest_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
