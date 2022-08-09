"""setuptools setup module for flask-gae-static.

Docs: https://setuptools.readthedocs.io/
"""
from setuptools import setup


setup(name='flask-gae-static',
      version='1.0',
      description='Flask extension that serves static file handlers in Google App Engine app.yaml files',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/snarfed/flask-gae-static',
      py_modules=['flask_gae_static'],
      author='Ryan Barrett',
      author_email='flask-gae-static@ryanb.org',
      license='Public domain',
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Environment :: Web Environment',
          'License :: OSI Approved :: MIT License',
          'License :: Public Domain',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Framework :: Flask',
      ],
      keywords=['flask', 'App Engine', 'Google App Engine', 'app.yaml',
                'static', 'files', 'directories'],
      install_requires=[
          'flask',
          'pyyaml',
          'werkzeug!=2.2.0,!=2.2.1',
      ],
)
