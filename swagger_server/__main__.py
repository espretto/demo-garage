#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./spec/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('garage.openapi.yml', arguments={'title': 'Stompyt Garage'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
