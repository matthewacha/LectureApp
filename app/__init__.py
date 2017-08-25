from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

loginmanager=LoginManager()

app=Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False

loginmanager.init_app(app)
loginmanager.login_message = "You need to be logged in to view this page"
loginmanager.login_view = "auth_login"


from app import models
from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .authentic import authentic as authentic_blueprint
app.register_blueprint(authentic_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)