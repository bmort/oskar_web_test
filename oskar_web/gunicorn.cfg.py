# coding: utf-8
"""Gunicorn configuration."""
import multiprocessing

# pylint: disable=invalid-name
bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
