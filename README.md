flask-gae-static ![unit tests badge](https://github.com/snarfed/flask-gae-static/actions/workflows/unit-tests.yml/badge.svg)
===

[Flask](https://flask.palletsprojects.com/) extension for [Google App Engine](https://cloud.google.com/appengine/) that serves static file handlers from [`app.yaml` files](https://cloud.google.com/appengine/docs/standard/python3/config/appref).

App Engine's built in static file serving is better in most ways than serving static files via app code: it uses Google Cloud's CDN, which is generally faster, cheaper, more scalable, and more secure. However, App Engine's [`dev_appserver` local server](https://cloud.google.com/appengine/docs/standard/python3/testing-and-deploying-your-app#local-dev-server) is [deprecated](https://cloud.google.com/appengine/docs/standard/python3/testing-and-deploying-your-app) and [degrading](https://issuetracker.google.com/issues?q=%22dev_appserver%22), and Google hasn't provided a replacement for local development that supports `app.yaml`-based static file handlers. This extension fills that gap.

Inspired by [Andreas H. Kelch](https://github.com/XeoN-GHMB)'s [app_server](https://github.com/XeoN-GHMB/app_server) project.

License: This project is placed in the public domain. You may also use it under the [CC0 public domain dedication](http://creativecommons.org/publicdomain/zero/1.0/).


Usage
---
Install with `pip install flask-gae-static`. Use with eg:

```py
from flask import Flask
import flask_gae_static

app = Flask(..., static_folder=None)
flask_gae_static.init_app(app)
...
```

(`static_folder=None` is required to disable Flask's [built in static file handling](https://flask.palletsprojects.com/en/2.2.x/tutorial/static/) so that flask-gae-static can handle static files under any URL path prefix.)

flask-gae-static also includes a custom [URL route converter](https://flask.palletsprojects.com/en/2.0.x/api/#url-route-registrations) that supports regular expressions. After calling `init_app()`, you can use it with `regex` inside a variable route part, eg:

```py
@app.route('/<regex("(abc|def)"):letters>')
def handle(letters):
  ...
```


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
### 1.0 - 2021-08-09

**Breaking changes**

Require the `Flask` app to be constructed with `static_folder=None`.

Before this, flask-gae-static tried to disable Flask's static file handling itself, but since it couldn't control the `Flask` initialization, it had to resort to workarounds that depended on Flask and werkzeug internal implementation details, and it broke when those details changed. This avoids that.

### 0.2 - 2021-12-31

Add support for regexp `url`s and regexp replacement strings in `static_files`.

### 0.1 - 2021-12-30

Initial release.
