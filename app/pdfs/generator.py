from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import  colors
from flask import current_app # Ruta base de tu aplicación
from reportlab.lib.utils import ImageReader # Libreria para agregar imagenes
from reportlab.lib.units import inch

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
    
    # Información del producto
    c.drawString(100, height - 100, f"Producto: {producto.name}")
    c.drawString(100, height - 130, f"Precio: {producto.precio}")
    
    # Configuración de la tabla de imágenes
    x_offset = 100    # Posición horizontal de inicio
    y_offset = height - 250  # Posición vertical de inicio (espacio para el título y precio)
    img_width, img_height = 100, 100  # Tamaño de cada imagen
    cols = 4  # Número de columnas
    padding = 10  # Espacio entre imágenes
    
    # Iterar sobre las imágenes y dibujarlas en una cuadrícula
    for i, img_name in enumerate(producto.imagenes[:8]):  # Limitar a 8 imágenes
        # Calcular la posición x e y para cada imagen
        col = i % cols
        row = i // cols
        x = x_offset + col * (img_width + padding)
        y = y_offset - row * (img_height + padding)
        
        # Ruta de la imagen actual
        ruta_imagen = os.path.join(current_app.root_path, 'productos', 'imagenes', img_name)
        
        # Verificar si la imagen existe antes de dibujarla
        if os.path.exists(ruta_imagen):
            img = ImageReader(ruta_imagen)
            c.drawImage(img, x, y, width=img_width, height=img_height)
        else:
            c.drawString(x, y + (img_height / 2), "Imagen no encontrada")
    

    c.save()
    return ruta_pdf
    





