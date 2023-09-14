from . import clientes
from flask import render_template,redirect,flash
from .forms import NuevoCliente, EditCliente
import app


@clientes.route('/crearCliente', methods=['GET','POST'])
def crear_cliente():
    p = app.models.Cliente()
    form = NuevoCliente()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        flash("Registro de cliente exitoso")
        return redirect('/clientes/listarCliente')

    return render_template('newCliente.html', form=form)


@clientes.route('/listarCliente')
def listar():
    clientes= app.Cliente.query.all()

    return render_template('listarCliente.html',
                           clientes=clientes)
    
    
    
@clientes.route('/editarCliente/<cliente_id>',
                methods=['GET','POST'])
def editar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    
    form_edit=EditCliente(obj = p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Actualizacion de cliente exitosa")
        return redirect('/clientes/listarCliente')
    return render_template('newCliente.html',
                           form=form_edit)
    
    
@clientes.route('/eliminarCliente/<cliente_id>',
                methods=['GET','POST'])
def eliminar(cliente_id):
     p = app.models.Cliente.query.get(cliente_id)
     app.db.session.delete(p)
     app.db.session.commit()
     flash("Cliente Eliminado")
     return redirect('/clientes/listarCliente')