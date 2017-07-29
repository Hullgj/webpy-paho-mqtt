try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = [
    'description': 'Car Counter',
    'author': 'Gavin Hull',
    'url': 'none',
    'download_url': 'none',
    'author_email': 'gjh9@kent.ac.uk',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mqtt_comm', 'app'],
    'name': 'report_parser'
]

setup(**config)