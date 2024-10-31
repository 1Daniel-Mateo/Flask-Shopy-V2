from . import auth
#el . es para que nos importe todo el modulo
from flask import render_template, redirect, flash
from .forms import LoginForm
import app
#se llama al modelo

#dependecias de autenticacion
from flask_login import current_user,login_user,logout_user 
#para comprobar al usuario actual

#ruta de login
@auth.route('/login',
            methods = ['GET','POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        # selecionar cliente
        c = app.models.Cliente.query.filter_by(userName = f.userName.data).first()
        if c is None or not c.check_password(f.password.data):
            flash("nombre o clave erronea")
            return redirect('/auth/login') 
        else:
            login_user(c, True)
            flash("bienvenido a la tabla clientes")
            return redirect('/clientes/listarCliente')
        
    return render_template("login.html",f=f)


#ruta de logout
@auth.route('/logout')
def logout():
    logout_user()
    flash("secion cerrada")
    return redirect('/auth/login')