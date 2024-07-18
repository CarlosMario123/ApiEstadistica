from flask import Blueprint, jsonify,current_app,request
from controllers.notifyController import send_email
NotyRoute = Blueprint("notify", __name__, url_prefix='/notify')

@NotyRoute.route("/",methods=["GET"])
def index():
    #notify/?problema="titulo problema"&descripcion="descripcion del problema"
    problema = request.args.get('problema')
    descripcion = request.args.get('descripcion')
    return send_email(problema,descripcion)
    
