#!/usr/bin/env bash
export FLASK_APP=oskar_web/app.py
export FLASK_DEBUG=True
export FLASK_ENV=development
flask run --host 0.0.0.0 --port 8080
