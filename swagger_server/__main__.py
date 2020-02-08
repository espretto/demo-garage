#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from .db import close_db


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='./spec/')
    
    flask_instance = app.app
    flask_instance.json_encoder = encoder.JSONEncoder
    flask_instance.teardown_appcontext(close_db)
    
    app.add_api('garage.openapi.yml', arguments={'title': 'Garage'})
    return app


if __name__ == '__main__':
    create_app().run(port=8080)
else:
    # publish wsgi app to be picked up by any
    # pre-fork production server e.g. gunicorn
    # application = create_app()
    pass 