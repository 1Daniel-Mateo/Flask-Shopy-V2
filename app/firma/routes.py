from . import firmas
from flask import render_template, redirect, flash, url_for
from .forms import Ingreso_firma, EditFirmaForm
import app#se llama al modelo
import os
from werkzeug.utils import secure_filename 

# Registro de firma
@firmas.route('/insertar', methods=['GET', 'POST'])
def registro_firma():
    p = app.models.Registro_firma()
    form = Ingreso_firma()
    
    if form.validate_on_submit():
        # Poblar el objeto Firma
        form.populate_obj(p)
        p.firmas = []

        # Guardar cada imagen
        for firma_field in form.firmas:
            if firma_field.data:
                filename = firma_field.data.filename
                # Guardar la imagen en el sistema de archivos
                firma_field.data.save(os.path.join('app/firma/static/firmas', filename))
                # Agregar el nombre de la imagen a la lista
                p.firmas.append(filename)

        # Agregar el firma a la base de datos
        app.db.session.add(p)
        app.db.session.commit()
        flash("Registro de firmas exitoso")
        return redirect('/clientes/listarCliente')
        
    return render_template('ingreso_firma.html', form=form)


@firmas.route('/lista_firmas')
def lista_firmas():
    firmas = app.Registro_firma.query.all()
    return render_template('lista_firma.html', firmas=firmas)


@firmas.route('/editar/<firma_id>', methods=['GET','POST'])
def editar(firma_id):
    # Seleccionar el firma con el Id
    f = app.models.Registro_firma.query.get(firma_id)
    
    # Cargo el formulario con los atributos del firma
    form_edit = EditFirmaForm(obj=f)
    
    # Cargar las imágenes actuales del firma en el formulario
    if not form_edit.firmas.entries:
        for img in f.firmas:
            form_edit.firmas.append_entry()

    if form_edit.validate_on_submit():
        form_edit.populate_obj(f)

        # Lista para almacenar nombres de nuevas imágenes
        nuevas_firmas = []
        
        # Guardar las nuevas imágenes o mantener las actuales si no se reemplazan
        for i, firma_field in enumerate(form_edit.firmas):
            if firma_field.data:
                # Verifica si es un archivo de imagen válido
                if hasattr(firma_field.data, 'filename') and firma_field.data.filename:
                    filename = secure_filename(firma_field.data.filename)
                    file_path = os.path.join('app/firma/static/firmas/', filename)
                    
                    # Guardar el archivo
                    firma_field.data.save(file_path)
                    nuevas_firmas.append(filename)
                else:
                    # Mantén la imagen actual si no se sube una nueva
                    nuevas_firmas.append(f.firmas[i])
            elif i < len(f.firmas):
                # Si no hay una nueva imagen, conservar la imagen actual
                nuevas_firmas.append(f.firmas[i])

        # Actualizar las imágenes en la base de datos
        f.firmas = nuevas_firmas
        app.db.session.commit()

        flash("Firma actualizada con éxito")
        return redirect('/firmas/lista_firmas')

    return render_template('editar_firma.html', form=form_edit, firma=f, enumerate=enumerate)
                         
    
   # return "EL firma id editar:"+ firma_id