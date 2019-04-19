from app import app
from flask import session,render_template,redirect,url_for, request
import bi.bi_index as bi_index

@app.route("/otro")
def otro():

    return bi_index.index()
