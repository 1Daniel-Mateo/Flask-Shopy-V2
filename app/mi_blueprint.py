from flask import Blueprint, send_file,redirect
from .pdf_generator import generar_pdf


#crear y configurar mmi blueprint 
mi_blueprint = Blueprint('mi_blueprint',
                         __name__,
                         url_prefix = '/ejemplo')

#Ruta de ejemplo de blueprint
@mi_blueprint.route('/bienvinido')

def bienvinido():
    return 'Usa audifonos por favor'


@mi_blueprint.route('/generar_pdf')
def crear_pdf():
    try:
        contenido = "Este es un acta de contenido para el PDF.\nPuedes agregar más líneas aquí."
        nombre_archivo = "acta.pdf"  # Asegúrate de que este es solo el nombre del archivo
        
        # Generar el PDF
        ruta_pdf = generar_pdf(nombre_archivo, contenido)
        
        return send_file(ruta_pdf, as_attachment=True)
    except Exception as e:
        print(f"Error al generar el PDF: {e}")  # Imprime el error para depuración
        return "Error al generar el PDF"


