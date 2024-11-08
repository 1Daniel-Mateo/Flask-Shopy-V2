from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField, FieldList,FormField#Tipos de datos d formulario
from flask_wtf.file import FileField, FileRequired,FileAllowed #Tipos de archivos que se van a cargar
from wtforms.validators import InputRequired, NumberRange,Optional #Validaciones de formulario


class Ingreso_firma(FlaskForm):
    name1 =  StringField("Responsable de Registraduría:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
    name2 = StringField("Responsable de Auditoría externa:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
    name3 = StringField("Responsable de Procuraduría:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
    name4 = StringField("Responsable de Procuraduría:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
    name5 = StringField("Responsable de Contratista:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
    firmas =  FieldList(FileField("Imagen de producto", validators=[
                            FileRequired(message="Debes ingresar un archivo"),
                            FileAllowed(['jpg', 'png','pdf'], message='Solo se admiten imágenes')
                         ]), min_entries=5, max_entries=5)
    
    
    submit = SubmitField('Guardar firma')
    
    
class EditFirmaForm(FlaskForm):
     name1 =  StringField("Responsable de Registraduría:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
     name2 = StringField("Responsable de Auditoría externa:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
     name3 = StringField("Responsable de Procuraduría:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
     name4 = StringField("Responsable de Procuraduría:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
     name5 = StringField("Responsable de Contratista:",
                        validators=[InputRequired(message="por favor ingresa un nombre de producto")])
     firmas =  FieldList(FileField("Imagen de producto", validators=[
                             Optional(),
                             FileAllowed(['jpg', 'png','pdf'], message='Solo se admiten imágenes')
                        ]), min_entries=5, max_entries=5)
    
     submit=SubmitField("Actualizar")