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
    releases_dir = join(path, 'static', 'releases')
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
    config = dict(new_release=True, releases=RELEASES,
                  downloads=[{'name': 'Telescope Models'}])
    return render_template('home.html', **config)


@APP.route('/releases/<version>')
def release(version):
    """."""
    config = dict(releases=RELEASES, version=version)
    return render_template('release.html', **config)


@APP.route('/faq')
def faq():
    """."""
    config = dict(releases=RELEASES)
    return render_template('faq.html', **config)


@APP.route('/documentation')
def documentation():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('documentation.html', **config)


@APP.route('/quick_start')
@APP.route('/start')
def getting_start():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('getting_started.html', **config)


@APP.route('/downloads')
def downloads():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('downloads.html', **config)


@APP.route('/releases')
def releases():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('releases.html', **config)

@APP.route('/data')
def data():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('data.html', **config)


@APP.route('/data/telescopes')
def telescope_models():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('telescope_models.html', **config)

@APP.route('/data/sky')
def sky_models():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('sky_models.html', **config)

@APP.route('/data/scripts')
def scripts():
    """."""
    config = dict(releaes=RELEASES)
    return render_template('scripts.html', **config)
