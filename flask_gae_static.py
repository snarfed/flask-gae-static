"""Flask extension for static files based on Google App Engine app.yaml files.

app.yaml reference docs:
https://cloud.google.com/appengine/docs/standard/python3/config/appref
"""
import logging
from pathlib import Path

from flask import current_app, send_from_directory, send_file
import yaml

logger = logging.getLogger(__name__)


def init_app(app):
    """Load app.yaml and register a URL rule for each static handler."""
    with open(Path(app.root_path) / 'app.yaml', 'r') as f:
        config = yaml.safe_load(f)

    for route in config.get('handlers', []):
        url = route['url']

        if path := route.get('static_dir'):
            if url == app.static_url_path:
                logger.warning(f"Overriding Flask's built in static handler for {url}")
                app.view_functions[app.static_url_path] = None
                for rule in app.url_map.iter_rules('static'):
                    app.url_map._rules.remove(rule)
                app.url_map._rules_by_endpoint['static'] = []

            rule = str(Path(url) / '<path:file>')
            logger.info(f'Registering {rule} to serve {path}/*')
            app.add_url_rule(rule, endpoint=path, view_func=static_dir(path))

        elif path := route.get('static_files'):
            logger.info(f'Registering {url} to serve {path}')
            app.add_url_rule(url, endpoint=path, view_func=static_file(path))


def static_dir(dir):
    def wrapped(file):
        return send_from_directory(Path(current_app.root_path) / dir, file)

    return wrapped


def static_file(path):
    def wrapped():
        return send_file(Path(current_app.root_path) / path)

    return wrapped
