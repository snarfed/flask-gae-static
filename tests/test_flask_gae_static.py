"""Unit tests for flask_gae_static.py."""
import os
from unittest import TestCase

from flask import Flask
import flask_gae_static


class TestFlaskGAEStatic(TestCase):
    def setUp(self):
        super().setUp()
        app = Flask('test', root_path=os.path.dirname(__file__), static_folder=None)
        flask_gae_static.init_app(app)

        @app.route('/')
        def home():
            return 'home'

        self.client = app.test_client()
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        super().tearDown()

    def test_routes(self):
        for path, status, contents in (
                ('/', 200, 'home'),
                ('/shrug', 404, None),
                ('/file.txt', 200, 'some text'),
                ('/file.txty', 404, None),
                ('/other/bar', 200, 'bar'),
                ('/other/biff', 404, None),
                ('/other/inner/baz', 200, 'baz'),
                ('/static/foo', 200, 'foo'),
                ('/static/phoo', 404, 'phoo'),
                ('/x.dat', 200, 'my-x'),
                ('/y.dat', 200, 'my-y'),
                ('/z.dat', 404, None),
        ):
            with self.subTest(path=path):
                resp = self.client.get(path)
                self.assertEqual(status, resp.status_code)
                if status == 200:
                    self.assertEqual(contents, resp.get_data(as_text=True).strip())
                resp.close()
