from datetime import datetime
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash,check_password_hash;
from app import db
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.mysql import JSON

#Modelos
class Cliente(UserMixin, db.Model):
    __tablename__= "clientes"
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, clave):
        return check_password_hash(self.password, clave) 
    
#En este decorador voy asignar el id de base de datos el id
#del usuario que se logeo
@login.user_loader
def user_loader(id):
     return Cliente.query.get(id)

class Producto(db.Model):
    __tablename__= "productos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10,scale =2 ))
    imagenes = db.Column(MutableList.as_mutable(JSON))


class Venta(db.Model):
    __tablename__= "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime,default=datetime.utcnow)
    cliente_id=db.Column(db.Integer, db.ForeignKey('clientes.id'))#La tabla en minuscula y linea para la conexion

class Detalle(db.Model):
     __tablename__= "detalles"
     id = db.Column(db.Integer, primary_key = True)
     produto_id=db.Column(db.Integer, db.ForeignKey('productos.id'))
     venta_id=db.Column(db.Integer, db.ForeignKey('ventas.id'))


class Registro_firma(db.Model):
    __tablename__ = "registro_firma"
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(150))
    name2 = db.Column(db.String(150))
    name3 = db.Column(db.String(150))
    name4 = db.Column(db.String(150))
    name5 = db.Column(db.String(150))
    firmas = db.Column(MutableList.as_mutable(JSON))
