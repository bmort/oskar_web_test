# coding: utf-8
"""WSGI application script (needed for Gunicorn)."""
from .app import APP as application

if __name__ == '__main__':
    application.run()
