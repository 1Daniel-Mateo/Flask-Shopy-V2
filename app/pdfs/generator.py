from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generar_pdf(nombre_archivo, contenido):        
    # Establecer la ruta del archivo PDF
    ruta_pdf = os.path.join('app','pdfs','static',nombre_archivo)
    
    # Creamos un objeto Canvas para el PDF
    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    width, height = letter
    
    #Contenido del pdf
    c.drawString(100, height - 100, "Contenido del PDF:")
    for i, linea in enumerate(contenido.splitlines(), start=1):
        c.drawString(100, height - (100 + i * 20), linea)
        
    c.save()
    return ruta_pdf
    





