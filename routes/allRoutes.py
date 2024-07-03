from routes.dhtRoute import dhtRoute

def instanceRoute(app):
    app.register_blueprint(dhtRoute)
