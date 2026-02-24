from flask import Flask
from pokemon.extnsins import db, login_manager, bcrypt
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clubs.db'
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    return app

