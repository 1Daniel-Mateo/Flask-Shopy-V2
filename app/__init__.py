from flask import Flask, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config
from flask_bootstrap import Bootstrap #estilo de bootstrap
from flask_login import LoginManager;

#blueprint
from .mi_blueprint import mi_blueprint
from app.pdfs import pdf
from app.productos import productos 
from app.clientes import clientes
from app.auth import auth

#Creación y configuración del app 
app = Flask(__name__)
app.config.from_object(Config)
b = Bootstrap(app)
login = LoginManager(app) 


#configurar y registrar blueprint
app.register_blueprint(mi_blueprint)
app.register_blueprint(pdf)
app.register_blueprint(productos)
app.register_blueprint(clientes)
app.register_blueprint(auth)
#Mensaje de seguridad para prevencion de ataques
app.config["SECRET_KEY"] = "lo que se quiera aqui..."

#Crear los objetos de SQLAlchemy y Migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#traemos los modelos 
from .models import Producto,Cliente,Venta,Detalle

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")

@app.route('/')
def home():
    return redirect('/auth/login')





