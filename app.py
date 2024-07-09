from flask import Flask
from routes.allRoutes import instanceRoute
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["1200 per day", "300 per hour"],
    storage_uri="memory://",
)



@app.route("/",methods=["GET"])
@limiter.limit("5 per minute")
def index():
    return "Bienvenido al control estadistico de avitech"

instanceRoute(app,limiter=limiter)
if __name__ == '__main__':
    app.run(debug=True)