from flask import Flask,render_template,session
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_pyfile('config.py')
mongo = PyMongo(app)

from controllers.indexController import *
from controllers.other import *

if __name__ == '__main__':
    IP = "localhost"#"192.168.0.123"
    PORT = 8080
    app.run(
        host=app.config.get("HOST", IP),
        port=app.config.get("PORT", PORT)
    )
