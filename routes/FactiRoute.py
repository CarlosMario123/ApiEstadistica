#endpoints para lo de la factibilidad
from flask import Blueprint, jsonify
from controllers.factiController import checkFactibility
factiRoute = Blueprint("factibilidad", __name__, url_prefix='/factibilidad')

@factiRoute.route("/",methods=["GET"])
def index():
    data = checkFactibility()
    
    return jsonify({"aguaConsumida":data})
    

