from app import app
from flask import session,render_template,redirect,url_for, request

from controllers.perfilController import *
from controllers.apiController import *
import models.indexModel as indexModel

@app.route("/")
def index():
    
    if 'user' in session:
        return render_template('dashboard.html')
    
    return render_template('login.html')
    
@app.route("/login",methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        indexModel.index(request.form['user'],request.form['password'])
        session['user'] = request.form['user']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return 'login entry'

@app.route("/logout",methods = ['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404