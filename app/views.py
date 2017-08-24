#views for the app
from flask import Flask
from app import app

@app.route('/index')
def hello_world():
 return 'Hello World'