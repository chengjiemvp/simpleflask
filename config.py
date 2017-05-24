import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Do you want to guess my key?'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[个人项目]'
    FLASKY_MAIL_SENDER = '765925079@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or '765925079@qq.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = os.environ.get( 'MAIL_USERNAME' ) or '765925079'
    MAIL_PASSWORD = os.environ.get( 'MAIL_PASSWORD' )
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:00@127.0.0.1:3306/simpleproject'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:00@127.0.0.1:3306/test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:00@127.0.0.1:3306/simpleproject'

config = {
    'development':DevelopmentConfig,
    'test':TestConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
    }
