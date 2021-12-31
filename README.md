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
### 0.1 - 2021-12-30

Initial release.
