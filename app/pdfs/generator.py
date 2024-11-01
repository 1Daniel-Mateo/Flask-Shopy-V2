from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import  colors
from flask import current_app # Ruta base de tu aplicación
from reportlab.lib.utils import ImageReader # Libreria para agregar imagenes

import os

def generar_pdf(nombre_archivo, producto):        
    # Establecer la ruta del archivo PDF
    ruta_pdf = os.path.join(current_app.root_path,'pdfs','static',nombre_archivo)
    
    # Crear la carpeta si no existe
    if not os.path.exists(os.path.dirname(ruta_pdf)):
        os.makedirs(os.path.dirname(ruta_pdf))  
        
    # Creamos un objeto Canvas para el PDF
    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    width, height = letter
    
    # Configuración de la fuente
    c.setFont("Helvetica-Bold", 16)
    
    #Contenido del pdf
    c.drawString(100, height - 100, f"Producto: {producto.name}")
    c.drawString(100, height - 130,  f"Precio: {producto.precio}")

    # Ruta de la imagen del producto
    ruta_imagen = os.path.join(current_app.root_path, 'productos','imagenes', producto.imagen)
    
    if os.path.exists(ruta_imagen):
        # Agregar la imagen al PDF
        img =  ImageReader(ruta_imagen)
        c.drawImage(img, 100, height - 350, width=200, height=200)
    else:
        c.drawString(100, height - 300, "No se encontró la imagen del producto")

    
    c.save()
    return ruta_pdf
    





