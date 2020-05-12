from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'authentication.login'
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    db.init_app(app)
    bootstrap = Bootstrap(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix = '/main')
    
    from .authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint,url_prefix = '/auth')

    
    return app