flask-gae-static ![unit tests badge](https://github.com/snarfed/flask-gae-static/actions/workflows/unit-tests.yml/badge.svg)
===

[Flask](https://flask.palletsprojects.com/) extension for [Google App Engine](https://cloud.google.com/appengine/) that serves static file handlers from [`app.yaml` files](https://cloud.google.com/appengine/docs/standard/python3/config/appref).

Inspired by [Andreas H. Kelch](https://github.com/XeoN-GHMB)'s [app_server](https://github.com/XeoN-GHMB/app_server) project.

License: This project is placed in the public domain. You may also use it under the [CC0 public domain dedication](http://creativecommons.org/publicdomain/zero/1.0/).


Usage
---
Install with `pip install flask-gae-static`. Use with eg:

```py
from flask import Flask
import flask_gae_static

app = Flask(...)
flask_gae_static.init_app(app)
...
```

flask-gae-static also includes a custom [URL route converter](https://flask.palletsprojects.com/en/2.0.x/api/#url-route-registrations) that supports regular expressions. After calling `init_app()`, you can use it with `regex` inside a variable route part, eg:

```py
@app.route('/<regex("(abc|def)"):letters>')
def handle(letters):
  ...
```


Known issues
---
* flask-gae-static currently only overrides [Flask's built in static file support](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask) if a static handler's URL exactly matches the Flask app's `static_url_path`. If the static handler URL is a regexp that overlaps with it, Flask's `static_url_path` handling will still take precedence.


Development
---
After cloning the repository, set up a local virtualenv with:

```py
python3 -m venv local
source local/bin/activate
pip install -e .
```

Run tests with:

```py
python -m unittest discover
```


Changelog
---
### 0.2 - 2021-12-31

Add support for regexp `url`s and regexp replacement strings in `static_files`.

### 0.1 - 2021-12-30

Initial release.
