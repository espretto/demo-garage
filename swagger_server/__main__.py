#!/usr/bin/env python3

import connexion
import yaml

from swagger_server import encoder
from .db import close_db


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='./spec/')
    
    flask_instance = app.app
    flask_instance.json_encoder = encoder.JSONEncoder
    flask_instance.teardown_appcontext(close_db)
    
    with (app.specification_dir / 'garage.openapi.yml').open('rt') as file:
        flask_instance.config['OPENAPI'] = yaml.load(file, Loader=yaml.FullLoader)

    app.add_api('garage.openapi.yml', arguments={'title': 'Garage'})
    return app


if __name__ == '__main__':
    create_app().run(port=8080)
else:
    # publish wsgi app to be picked up by any
    # pre-fork production server e.g. gunicorn
    # application = create_app()
    pass 