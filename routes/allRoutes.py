from routes.dhtRoute import dhtRoute
from routes.FactiRoute import factiRoute

def instanceRoute(app):
    app.register_blueprint(factiRoute)
    app.register_blueprint(dhtRoute)
