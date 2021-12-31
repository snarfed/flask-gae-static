"""setuptools setup module for flask-gae-static.

Docs: https://setuptools.readthedocs.io/
"""
from setuptools import setup, find_packages


setup(name='flask-gae-static',
      version='0.1',
      description='Flask extension that serves static file handlers in Google App Engine app.yaml files',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/snarfed/flask-gae-static',
      py_modules=['flask-gae-static'],
      author='Ryan Barrett',
      author_email='flask-gae-static@ryanb.org',
      license='Public domain',
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
      ],
      keywords='flask app-engine static files app.yaml',
      install_requires=[
          'flask',
          'pyyaml',
      ],
)
