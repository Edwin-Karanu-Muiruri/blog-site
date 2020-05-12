import os

class Config:
    '''
    Parent config class
    '''
    SECRET_KEY = 'EdwinKaranu'

class DevConfig(Config):
    '''
    Development child config class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://edwin:EDUcaranow98@localhost/personalblog'
    DEBUG = True

class ProdConfig(Config):
    '''
    Production config class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    
config_options = {
    'production' :ProdConfig,
    'development' :DevConfig
}
