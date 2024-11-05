from . import productos
#el . es para que nos importe todo el modulo
from flask import render_template, redirect, flash
from .forms import NuevoProducto,EditProdForm, Registro_firma
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
    
    return render_template('new.html', form=form)


@productos.route('/listar')
def listar():
   #Traeremos los productos  de la base de datos
   productos = app.Producto.query.all()
   #mostrar la vista de listar
   #envieandole los productos seleccionados
   return render_template('listar.html',
                          productos=productos)
   
   
@productos.route('/editar/<producto_id>',
                 methods=['GET','POST'])
def editar(producto_id):
   #Seleccionar producto con el Id
   p = app.models.Producto.query.get(producto_id)
   #Cargo el formulario con los atributo del producto
   form_edit=EditProdForm(obj = p)
   if form_edit.validate_on_submit():
      form_edit.populate_obj(p)
      app.db.session.commit()
      flash("Producto Actualizado")
      return redirect('/productos/listar')
   return render_template('new.html',
                          form = form_edit)
    
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

# Registro de firma
@productos.route('/firma', methods=['GET', 'POST'])
def registro_firma():
    p = app.models.Registro()
    form = Registro_firma()
    
    if form.validate_on_submit():
        # Poblar el objeto Producto
        form.populate_obj(p)
        p.firmas = []

        # Guardar cada imagen
        for firma_field in form.firmas:
            if firma_field.data:
                filename = firma_field.data.filename
                # Guardar la imagen en el sistema de archivos
                firma_field.data.save(os.path.join('app/productos/static', filename))
                # Agregar el nombre de la imagen a la lista
                p.firmas.append(filename)

        # Agregar el producto a la base de datos
        app.db.session.add(p)
        app.db.session.commit()
        flash("Registro de firmas exitoso")
        return redirect('/clientes/listarCliente')
        
    return render_template('registro.html', form=form)
        
    
   
   
   
   