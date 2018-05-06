# -*- coding: utf-8 -*-
import os
from os.path import join
from pprint import pprint
from flask import Flask, render_template
from datetime import datetime, date


APP = Flask(__name__)

DATA = {
    "current_release": "2.5.1",
    "release_path": "/static/releases",
    "doc_ext": ".pdf",
    "releases": {
        "2.7.0":
        {
            "date": "05/05/18",
        },
        "2.6.1":
        {
            "date": "05/06/17",
        },
        "2.5.1":
        {
            "date": "05/06/16",
            "docs": [
                "Apps",
                "Binary-File-Format",
                "Example",
                "Install",
            ]
        }
    }
}


@APP.route('/')
def home():
    """."""
    now = datetime.now()
    version = DATA['current_release']
    _date = DATA['releases'][version]['date']
    delta = now - datetime.strptime(DATA['releases'][version]['date'], '%d/%m/%y')
    new_release = True if delta.days < 30 else False
    return render_template('home.html',
                           new_release=new_release,
                           data=DATA)



@APP.route('/faq')
def faq():
    """."""
    return render_template('faq.html',
                           data=DATA)


@APP.route('/documentation')
def documentation():
    """."""
    _path = os.path.join(DATA['release_path'], DATA['current_release'], 'docs')
    _version = '.'.join(DATA['current_release'].split('.')[:2])
    return render_template('documentation.html',
                           doc_path=_path,
                           doc_version=_version,
                           data=DATA)


@APP.route('/quick_start')
@APP.route('/start')
def getting_start():
    """."""
    return render_template('getting_started.html',
                           data=DATA)


@APP.route('/downloads')
def downloads():
    """."""
    return render_template('downloads.html',
                           data=DATA)


@APP.route('/downloads/<version>')
def release(version):
    """."""
    return render_template('release.html',
                           data=DATA,
                           version=version)


@APP.route('/downloads/telescopes')
def telescope_models():
    """."""
    return render_template('telescope_models.html',
                           data=DATA)


@APP.route('/downloads/sky')
def sky_models():
    """."""
    return render_template('sky_models.html',
                           data=DATA)


@APP.route('/downloads/scripts')
def scripts():
    """."""
    return render_template('scripts.html',
                           data=DATA)
