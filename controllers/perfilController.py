from app import app
from flask import session,render_template,redirect,url_for, request
import models.perfilModel as perfilModel

@app.route("/perfil",methods = ['POST', 'GET'])
def perfil():
	if 'user' in session:
		data = perfilModel.index(session['user'])
		return render_template('perfil/perfil.html',data = data)
	return redirect(url_for('index'))

@app.route("/editarPerfil",methods = ['POST', 'GET'])
def editarPerfil():
     if 'user' in session:
        return render_template('perfil/editarperfil.html')
     return redirect(url_for('index'))

@app.route("/guardarPerfil",methods = ['POST', 'GET'])
def guardarPerfil():
     if 'user' in session:
          return redirect(url_for('perfil'))
     return redirect(url_for('index'))