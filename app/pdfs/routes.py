from flask import render_template, send_file, current_app
from . import pdf
from .generator import  generar_pdf

@pdf.route('/generar_pdf')
def crear_pdf():
    try:
        contenido = "Este es un acta de contenido para el PDF.\nPuedes agregar más líneas aquí."
        nombre_archivo = "acta.pdf"  # Asegúrate de que este es solo el nombre del archivo
        
        # Generar el PDF
        ruta_pdf = generar_pdf(nombre_archivo, contenido)
        
        return send_file(ruta_pdf, as_attachment=True, mimetype='application/pdf')
    except Exception as e:
        print(f"Error al generar el PDF: {e}")  # Imprime el error para depuración
        return "Error al generar el PDF"
