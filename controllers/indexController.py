from app import app
from flask import session,render_template,redirect,url_for, request
import models.indexModel as indexModel

@app.route("/")
def index():
    if 'user' in session:
        return render_template('dashboard.html')
    
    return render_template('login.html')
    
@app.route("/login",methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return 'login entry'

@app.route("/logout",methods = ['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))