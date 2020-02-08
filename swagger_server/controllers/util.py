
import connexion
from flask import current_app


def api_base_url():
    spec = current_app.config['OPENAPI']
    host = spec.get('host', connexion.request.host)
    return 'http://{}{}'.format(host, spec['basePath'])


__all__ = ['api_base_url']