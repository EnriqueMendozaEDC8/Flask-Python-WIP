from app import app
from flask import session,render_template,redirect,url_for, request
import models.consumirApi as ca

@app.route("/api")
def api():
    cadena = ca.consumirApi()
    return cadena