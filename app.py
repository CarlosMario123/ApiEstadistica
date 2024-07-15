from flask import Flask, render_template
from routes.allRoutes import instanceRoute
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from pymongo import MongoClient


# Configuración de MongoDB
client = MongoClient("mongodb://44.194.109.225:27017/") 
db = client["ips"]  #base de datos
collection = db["rate_limit_data"]  

app = Flask(__name__)


# Configuración de Flask-Limiter con MongoDB como backend
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["1200 per day", "300 per hour"],
    storage_uri=f"mongodb://44.194.109.225:27017/ips" 
)

@app.route("/", methods=["GET"])
@limiter.limit("5 per minute")
def index():
    return render_template("index.html")


instanceRoute(app, limiter=limiter)

if __name__ == '__main__':
    app.run(debug=True)

