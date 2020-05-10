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

class ProdConfig(COnfig):
    '''
    Production config class
    '''

production = 'ProdConfig'
development = 'DevConfig'
