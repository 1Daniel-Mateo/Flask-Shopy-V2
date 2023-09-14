from . import productos
#el . es para que nos importe todo el modulo
from . import productos
from flask import render_template, redirect, flash
from .forms import NuevoProducto,EditProdForm
import app#se llama al modelo
import os 

@productos.route('/crear', methods=["GET","POST"])
def crear_producto():
    p = app.models.Producto()
    form=NuevoProducto()
    if form.validate_on_submit():
       #El formulario va a llenar
       #El nuevo objeto producto
       #automaticamente
       form.populate_obj(p)
       p.imagen=form.imagen.data.filename
       app.db.session.add(p)
       app.db.session.commit()
       
       #Ubicar el archivo imagen
       #se ubicara en app/productos/imagenes
       file = form.imagen.data
       file.save(os.path.abspath(os.getcwd()+'/app/productos/imagenes/'+p.imagen))
       flash("Regitro de producto exitoso")
       return redirect('/productos/listar')
       
    return render_template('new.html', form = form)


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


   