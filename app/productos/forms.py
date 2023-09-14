from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField#Tipos de datos d formulario
from flask_wtf.file import FileField, FileRequired,FileAllowed#Tipos de archivos que se van a cargar
from wtforms.validators import InputRequired, NumberRange #Validaciones de formulario

class ProductForm():
   name = StringField("Nombre del producto:",
                       validators= [InputRequired(message="por favor ingresa un nombre de producto")])
   
   precio = IntegerField("Precio del producto:", 
                        validators=[InputRequired(message="por favor ingresa un precio"),
                                    NumberRange(message="El precio esta fuera del rango", 
                                                min=10000, max=100000)])
    

#Definir el formulario de registro de productos

class NuevoProducto(FlaskForm, ProductForm):
    imagen =FileField(validators=[FileRequired(message="Debes ingresar un archivo"),
                                   FileAllowed(['jpg','png'],
                                               message='solo se admiten imagenes')],
                      label="Ingresa la imagen de producto:")
    
    submit = SubmitField("Registrar Producto")
    
#Formulario de editar producto    
class EditProdForm(FlaskForm, ProductForm):
    submit=SubmitField("Actualizar")