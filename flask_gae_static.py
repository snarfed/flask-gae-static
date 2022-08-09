"""Flask extension for static files based on Google App Engine app.yaml files.

app.yaml reference docs:
https://cloud.google.com/appengine/docs/standard/python3/config/appref
"""
import logging
from pathlib import Path
import re

from flask import current_app, request, send_file, send_from_directory
from werkzeug.routing import BaseConverter
import yaml

logger = logging.getLogger(__name__)


def init_app(app):
    """Load app.yaml and register a URL rule for each static handler."""
    assert app.static_folder is None, 'flask-gae-static requires the Flask app to be constructed with static_folder=None.'

    app.url_map.converters['regex'] = RegexConverter

    with open(Path(app.root_path) / 'app.yaml', 'r') as f:
        config = yaml.safe_load(f)

    for route in config.get('handlers', []):
        dir = route.get('static_dir')
        files = route.get('static_files')
        url = route['url']

        if not dir and not files:
            continue

        if dir:
            rule = str(Path(url) / '<path:file>')
            logger.info(f'Registering {rule} to serve {dir}/*')
            app.add_url_rule(rule, endpoint=url, view_func=static_dir(dir))

        elif files:
            rule = f'/<regex("{url.lstrip("/")}"):_>'
            logger.info(f'Registering {rule} to serve {files}')
            app.add_url_rule(rule, endpoint=url, view_func=static_file(url, files))


def static_dir(dir):
    def wrapped(file):
        return send_from_directory(Path(current_app.root_path) / dir, file)

    return wrapped


def static_file(url_pattern, files_replacement):
    def wrapped(_):
        path = (Path(current_app.root_path) /
                re.sub(url_pattern, files_replacement, request.path))
        return send_file(path) if path.exists() else ('', 404)

    return wrapped


class RegexConverter(BaseConverter):
  """Regexp URL route for Werkzeug/Flask.

  Based on https://github.com/rhyselsmore/flask-reggie.

  Usage: @app.route('/<regex("(abc|def)"):letters>')

  Install with:
    app = Flask(...)
    app.url_map.converters['regex'] = RegexConverter
  """
  def __init__(self, url_map, *items):
    super(RegexConverter, self).__init__(url_map)
    self.regex = items[0]
