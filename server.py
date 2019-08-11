from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']='thisismysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'

    db.init_app(app)

    from .pages import pages as pagesBlueprint
    app.register_blueprint(pagesBlueprint)