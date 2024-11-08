from . import productos
#el . es para que nos importe todo el modulo
from flask import render_template, redirect, flash
from .forms import NuevoProducto,EditProdForm
import app#se llama al modelo
import os 
from werkzeug.utils import secure_filename

@productos.route('/crear', methods=["GET","POST"])
def crear_producto():
    p = app.models.Producto()
    form = NuevoProducto()
    
    if form.validate_on_submit():
        # Poblar el objeto Producto
        form.populate_obj(p)
        p.imagenes = []

        # Guardar cada imagen
        for imagen_field in form.imagenes:
            if imagen_field.data:
                filename = imagen_field.data.filename
                # Guardar la imagen en el sistema de archivos
                imagen_field.data.save(os.path.join('app/productos/imagenes', filename))
                # Agregar el nombre de la imagen a la lista
                p.imagenes.append(filename)

        # Agregar el producto a la base de datos
        app.db.session.add(p)
        app.db.session.commit()
        flash("Registro de producto exitoso")
        return redirect('/productos/listar')
    
    return render_template('registro.html', form=form)


@productos.route('/listar')
def listar():
   #Traeremos los productos  de la base de datos
   productos = app.Producto.query.all()
   #mostrar la vista de listar
   #envieandole los productos seleccionados
   return render_template('listar.html',
                          productos=productos)
   
@productos.route('/editar/<producto_id>', methods=['GET','POST'])
def editar(producto_id):
    # Seleccionar el producto con el Id
    p = app.models.Producto.query.get(producto_id)
    
    # Cargo el formulario con los atributos del producto
    form_edit = EditProdForm(obj=p)
    
    # Cargar las imágenes actuales del producto en el formulario
    if not form_edit.imagenes.entries:
        for img in p.imagenes:
            form_edit.imagenes.append_entry()

    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)

        # Lista para las nuevas imágenes
        nuevas_imagenes = []
        
        # Guardar nuevas imágenes
        for i, imagen_field in enumerate(form_edit.imagenes):
            if imagen_field.data:
                if hasattr(imagen_field.data, 'filename') and imagen_field.data.filename:
                    # Si hay una nueva imagen, guardarla
                    filename = secure_filename(imagen_field.data.filename)
                    file_path = os.path.join('app/productos/imagenes', filename)
                    imagen_field.data.save(file_path)
                    nuevas_imagenes.append(filename)
                else:
                    # Si no es un archivo válido, manejar el error o continuar
                    nuevas_imagenes.append(p.imagenes[i])
            elif i < len(p.imagenes):
                # Si no se ha subido una nueva imagen, mantener la imagen actual
                nuevas_imagenes.append(p.imagenes[i])

        # Actualizar las imágenes en la base de datos
        p.imagenes = nuevas_imagenes
        app.db.session.commit()

        flash("Producto actualizado")
        return redirect('/productos/listar')

    return render_template('editar.html', form=form_edit, producto=p, enumerate=enumerate)
                         
    
   # return "EL producto id editar:"+ producto_id
   
    
@productos.route('/eleminar/<producto_id>',
                 methods=['GET','POST'])
def eliminar(producto_id):
   #Seleccionar producto con el Id
   p = app.models.Producto.query.get(producto_id)
   app.db.session.delete(p)
   app.db.session.commit()
   flash("Producto Eliminar")
   return redirect('/productos/listar')
   
   # return "El producto es id eliminar:"+producto_id


        
    
   
   
   
   