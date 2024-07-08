#endpoints para lo de la factibilidad
from flask import Blueprint, jsonify,current_app
from controllers.factiController import checkFactibility,checkFactFood


factiRoute = Blueprint("factibilidad", __name__, url_prefix='/factibilidad')



@factiRoute.route("/water",methods=["GET"])
def getWater():
    data = checkFactibility()
    
    return jsonify({"aguaConsumida":data})


@factiRoute.route("/food",methods=["GET"])
def getFood():
    data = checkFactFood()
    return jsonify({"Alimento consumido":data})
    
    
    

