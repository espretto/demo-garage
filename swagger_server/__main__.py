#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def create_app():
    app = connexion.App(__name__, specification_dir='./spec/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('garage.openapi.yml', arguments={'title': 'Stompyt Garage'})
    return app


if __name__ == '__main__':
    create_app().run(port=8080)
else:
    # publish wsgi app to be picked up by any
    # pre-fork production server e.g. gunicorn
    # application = create_app()
    pass 