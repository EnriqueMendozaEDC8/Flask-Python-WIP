from flask import Flask,render_template,session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_pyfile('config.py')

from controllers.indexController import *
from controllers.other import *

if __name__ == '__main__':
    app.run()
