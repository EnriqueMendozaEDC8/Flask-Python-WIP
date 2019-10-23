from app import app
import models.jsonEncoder as je
from flask_pymongo import PyMongo

mongo = PyMongo(app)
app.json_encoder = je.JSONEncoder

def index(userName):
    userData = mongo.db.infousers.find({'user':userName})
    for document in userData:
        return document