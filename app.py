from flask import Flask
from routes.allRoutes import instanceRoute

app = Flask(__name__)


@app.route("/",methods=["GET"])
def index():
    return "Bienvenido al control estadistico de avitech"

instanceRoute(app)
if __name__ == '__main__':
    app.run(debug=True)