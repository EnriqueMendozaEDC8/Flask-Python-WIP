from app import app
import models.jsonEncoder as je
from flask_pymongo import PyMongo

mongo = PyMongo(app)
app.json_encoder = je.JSONEncoder

def index(userName,password):
    user = mongo.db.users.find_one_or_404({"username":userName,"pass":password})
    return user
    """ return "i'm in bi folder and views" """