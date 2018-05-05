# -*- coding: utf-8 -*-
import os
from os.path import join
from pprint import pprint
from flask import Flask, render_template


APP = Flask(__name__)


def _get_releases():
    """."""
    print('here')
    path = os.path.dirname(__file__)
    releases = []
    releases_dir = join(path, 'assets', 'releases')
    for release_dir in sorted(os.listdir(releases_dir), reverse=True):
        if release_dir in ['.DS_Store']:
            continue
        doc_dir = join(releases_dir, release_dir, 'docs')
        docs = []
        for _file in os.listdir(doc_dir):
            if os.path.splitext(_file)[1] == '.pdf':
                docs.append(_file)
        releases.append(dict(version=release_dir, docs=docs))
    pprint(releases)
    return releases


RELEASES = _get_releases()

@APP.route('/')
def home():
    """."""
    config=dict(new_release=True, releases=RELEASES)
    return render_template('home.html', **config)

@APP.route('/<version>')
def release(version):
    """."""
    config=dict(releases=RELEASES)
    return render_template('release.html', **config)

@APP.route('/about')
def about():
    """."""
    config=dict(releases=RELEASES)
    return render_template('about.html', **config)