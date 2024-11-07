from flask import flash, render_template, send_file, current_app,redirect
from . import pdf
from .generator import  generar_pdf
import zipfile
import os

@pdf.route('/generar_pdf/<int:producto_id>')
def crear_pdf(producto_id):
    try:
        # Importar Producto aquí en lugar de al inicio
        from app.models import Producto, Registro_firma
        producto = Producto.query.get_or_404(producto_id)
        firma = Registro_firma.query.first()
        nombre_archivo = f"{producto.name}_prueba.pdf"  # Asegúrate de que este es solo el nombre del archivo
        
        # Generar el PDF
        ruta_pdf = generar_pdf(nombre_archivo, firma, producto)
        
        return send_file(ruta_pdf, as_attachment=True, mimetype='application/pdf')
        
    except Exception as e:
        print(f"Error generando PDF: {e}") 
        flash("No se pudo generar el PDF. Inténtalo de nuevo más tarde.")
        return redirect('productos/listar')
         

@pdf.route('/generar_todos_pdfs', methods=['POST'])
def generar_todos_pdfs():
    try:
        # Importar Producto y firma
        from app.models import Producto, Registro_firma
        productos = Producto.query.all()
        firma = Registro_firma.query.first()
        
        if not firma:
            flash("No hay firma registrada")
            return redirect('/productos/listar')

        
        #Generar PDF para cada producto
        rutas_pdf = []
        for producto in productos:
            #Llamamos a la función generar_pdf
            try:
                nombre_archivo = f"{producto.name}_prueba.pdf"
                ruta_pdf = generar_pdf(nombre_archivo, firma, producto)
                rutas_pdf.append(ruta_pdf)
            except Exception as e:
                print(f"Error generando PDF para {producto.name}: {e}")
                flash(f"Error generando PDF para {producto.name}.")
                
        
        zip_file = os.path.join(current_app.root_path,'pdfs','tmp','actas_pdfs.zip')
        with zipfile.ZipFile(zip_file, 'w') as zip_ref:
            for ruta_pdf in rutas_pdf:
                zip_ref.write(ruta_pdf, os.path.basename(ruta_pdf)) # Añadir el archivo al zip
                
        # Limpiar los archivos PDF temporales
        for ruta_pdf in rutas_pdf:
            os.remove(ruta_pdf)
            
        flash(f"Se han generado {len(productos)} PDFs exitosamente")
        return send_file(zip_file, as_attachment=True, mimetype='application/zip', download_name='actas_pdfs.zip')
    
    except Exception as e:
        print(f"Error generando PDF: {e}")
        return redirect('/productos/listar')
    
    