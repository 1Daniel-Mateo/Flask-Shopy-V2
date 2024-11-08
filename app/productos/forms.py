from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField, FieldList,FormField#Tipos de datos d formulario
from flask_wtf.file import FileField, FileRequired,FileAllowed #Tipos de archivos que se van a cargar
from wtforms.validators import InputRequired, NumberRange, Optional #Validaciones de formulario

class ProductForm():
    name = StringField("Nombre del producto:",
                       validators= [InputRequired(message="por favor ingresa un nombre de producto")])
   
    precio = IntegerField("Precio del producto:", 
                        validators=[InputRequired(message="por favor ingresa un precio"),
                                    NumberRange(message="El precio esta fuera del rango", 
                                                min=10000, max=100000)])
    

#Definir el formulario de registro de productos
class NuevoProducto(FlaskForm, ProductForm):
    imagenes = FieldList(FileField("Imagen de producto", validators=[
                            FileRequired(message="Debes ingresar un archivo"),
                            FileAllowed(['jpg', 'png'], message='Solo se admiten imágenes')
                         ]), min_entries=8, max_entries=8)
    

    
    submit = SubmitField("Registrar Producto")
    
#Formulario de editar producto    
class EditProdForm(FlaskForm, ProductForm):
    imagenes = FieldList(FileField("Imagen de producto", validators=[
                            Optional(),
                            FileAllowed(['jpg', 'png'], message='Solo se admiten imágenes')
                         ]), min_entries=8, max_entries=8)
    
    submit=SubmitField("Actualizar")
    




    
    
    