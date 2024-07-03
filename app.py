from flask import Flask
from routes.allRoutes import instanceRoute


app = Flask(__name__)

instanceRoute(app)
if __name__ == '__main__':
    app.run(debug=True)