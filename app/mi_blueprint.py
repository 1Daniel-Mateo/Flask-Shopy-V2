from flask import Blueprint

#crear y configurar mmi blueprint 
mi_blueprint = Blueprint('mi_blueprint',
                         __name__,
                         url_prefix = '/ejemplo')

#Ruta de ejemplo de blueprint
@mi_blueprint.route('/bienvinido')

def bienvinido():
    return 'Usa audifonos por favor'


