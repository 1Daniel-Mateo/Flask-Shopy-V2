from . import firmas
from flask import render_template, redirect, flash
from .forms import Ingreso_firma
import app#se llama al modelo
import os 

# Registro de firma
@firmas.route('/insertar', methods=['GET', 'POST'])
def registro_firma():
    p = app.models.Registro_firma()
    form = Ingreso_firma()
    
    if form.validate_on_submit():
        # Poblar el objeto Producto
        form.populate_obj(p)
        p.firmas = []

        # Guardar cada imagen
        for firma_field in form.firmas:
            if firma_field.data:
                filename = firma_field.data.filename
                # Guardar la imagen en el sistema de archivos
                firma_field.data.save(os.path.join('app/firma/static', filename))
                # Agregar el nombre de la imagen a la lista
                p.firmas.append(filename)

        # Agregar el producto a la base de datos
        app.db.session.add(p)
        app.db.session.commit()
        flash("Registro de firmas exitoso")
        return redirect('/clientes/listarCliente')
        
    return render_template('ingreso_firma.html', form=form)