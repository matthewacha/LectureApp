from flask import Flask
from flask_login import LoginManager
loginmanager=LoginManager()

app=Flask(__name__)
app.config.from_object('config')
loginmanager.init_app(app)
loginmanager.loginm_message = "You need to be logged in to view this page"
loginmanager.login_view = "auth_login"

from app import views