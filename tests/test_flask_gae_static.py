"""Unit tests for flask_gae_static.py."""
import os
from unittest import TestCase

from flask import Flask
import flask_gae_static


class TestFlaskGAEStatic(TestCase):
    def setUp(self):
        super().setUp()
        app = Flask('test_flask_gae_static', root_path=os.path.dirname(__file__))
        flask_gae_static.init_app(app)

        @app.route('/')
        def home():
            return 'home'

        self.client = app.test_client()
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        super().tearDown()

    def test_normal_route(self):
        for path, contents in (
                ('/', 'home'),
                ('/file.txt', 'some text'),
                ('/other/bar', 'bar'),
                ('/other/inner/baz', 'baz'),
                ('/static/foo', 'foo'),
        ):
            with self.subTest(path=path):
                resp = self.client.get(path)
                self.assertEqual(200, resp.status_code)
                self.assertEqual(contents, resp.get_data(as_text=True).strip())
                resp.close()
