from routes.dhtRoute import dhtRoute
from routes.FactiRoute import factiRoute
from routes.NotifyRoute import NotyRoute

def instanceRoute(app,limiter):
    app.register_blueprint(factiRoute)
    limiter.limit("5 per minute")(factiRoute)
    app.register_blueprint(dhtRoute)
    limiter.limit("5 per minute")(dhtRoute)
    app.register_blueprint(NotyRoute)
    limiter.limit("30 per minute")(NotyRoute)