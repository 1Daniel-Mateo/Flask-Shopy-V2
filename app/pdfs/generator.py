from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import  colors
# from reportlab.lib.utils import  ImageReader
import os

def generar_pdf(nombre_archivo, producto):        
    # Establecer la ruta del archivo PDF
    ruta_pdf = os.path.join('app','pdfs','static',nombre_archivo)
    
    # Creamos un objeto Canvas para el PDF
    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    width, height = letter
    
    # Configuración de la fuente
    c.setFont("Helvetica-Bold", 16)
    
    #Contenido del pdf
    c.drawString(100, height - 100, f"Producto: {producto.name}")
    c.drawString(100, height - 130,  f"Precio: {producto.precio}")

    
    c.save()
    return ruta_pdf
    





