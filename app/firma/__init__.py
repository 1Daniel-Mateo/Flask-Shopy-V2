from flask import Blueprint

firmas = Blueprint('firmas', 
                   __name__, 
                   url_prefix= '/firmas', 
                   template_folder='templates',
                   static_folder='static')

from . import routes
