from flask import Blueprint

productos = Blueprint('produtos',
                        __name__,
                        url_prefix= '/productos',
                        template_folder='templates',
                        static_folder='imagenes')
from . import routes
