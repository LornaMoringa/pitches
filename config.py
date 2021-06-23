import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = ''
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}