from routes.dhtRoute import dhtRoute
from routes.FactiRoute import factiRoute

def instanceRoute(app,limiter):
    app.register_blueprint(factiRoute)
    limiter.limit("5 per minute")(factiRoute)
    app.register_blueprint(dhtRoute)
    limiter.limit("5 per minute")(dhtRoute)
