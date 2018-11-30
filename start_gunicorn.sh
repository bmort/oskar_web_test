#!/usr/bin/env bash
gunicorn -c oskar_web/gunicorn.cfg.py oskar_web.wsgi
