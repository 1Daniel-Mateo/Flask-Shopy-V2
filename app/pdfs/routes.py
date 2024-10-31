from flask import flash, render_template, send_file, current_app,redirect
from . import pdf
from .generator import  generar_pdf


@pdf.route('/generar_pdf/<int:producto_id>')
def crear_pdf(producto_id):
    try:
        # Importar Producto aquí en lugar de al inicio
        from app.models import Producto
        producto = Producto.query.get_or_404(producto_id)
        nombre_archivo = f"{producto.name}_prueba.pdf"  # Asegúrate de que este es solo el nombre del archivo
        
        # Generar el PDF
        ruta_pdf = generar_pdf(nombre_archivo, producto)
        
        return send_file(ruta_pdf, as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        flash("No se pudo generar el PDF. Inténtalo de nuevo más tarde.")
        return redirect('/productos/listar')
         
