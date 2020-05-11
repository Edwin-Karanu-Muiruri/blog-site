class Config:
    '''
    Parent config class
    '''
    SECRET_KEY = 'EdwinKaranu'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://edwin@EDUcaranow98@localhost/personalblog'

class DevConfig(Config):
    '''
    Development child config class
    '''
    DEBUG = True

class ProdConfig(Config):
    '''
    Production config class
    '''
config_options = {
    production = 'ProdConfig',
    development = 'DevConfig'
}
