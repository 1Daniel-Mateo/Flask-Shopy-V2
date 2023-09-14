from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import InputRequired

#Formulario Maestro de cliente
class ClienteForm():
     userName=StringField("Nombre del cliente:",
                       validators= [InputRequired(message="por favor ingresa un nombre de cliente")])
     
     email=EmailField("Correo de cliente:",
                       validators= [InputRequired(message="por favor ingresa el correo del cliente")])
     
     password=PasswordField("Contraseña de cliente:",
                       validators= [InputRequired(message="por favor ingresa la contraseña del cliente")])
    

class NuevoCliente(FlaskForm,ClienteForm):
    submit = SubmitField("Registrar Cliente")
    
class EditCliente(FlaskForm,ClienteForm):
    submit = SubmitField("Actualizar")    
    
