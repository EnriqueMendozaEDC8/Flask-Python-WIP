from app import app
from flask import session,render_template,redirect,url_for, request
import models.indexModel as indexModel

@app.route("/otro")
def otro():

    return indexModel.index()
