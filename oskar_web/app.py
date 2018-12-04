# -*- coding: utf-8 -*-
"""OSKAR website Flask application script."""
import os
from multiprocessing.pool import ThreadPool

from flask import Flask, jsonify, render_template

APP = Flask(__name__)


def query_github():
    """Query github to get OSKAR release and repo metadata.

    At the moment this saves to a file but should probably update a database.
    """
    import time
    import github3
    import os
    import pickle
    data_file = 'oskar_github_meta.pickle'
    # if os.path.exists('oskar_github_meta.pickle'):
    #     print('LOADING DATA')
    #     load_start = time.time()
    #     with open(data_file, 'rb') as _file:
    #         data = pickle.load(_file)
    #     print('complete in {:4f} s'.format(time.time() - load_start))
    #     return 'Loaded'
    # else:
    _token = os.environ.get('GITHUB_OSKAR_WEB_TOKEN')
    print(_token)
    gh = github3.login(token=_token)
    repository = gh.repository(owner='OxfordSKA',
                               repository="OSKAR")
    latest_release = repository.latest_release()
    print("REMAINING RATE LIMIT...", latest_release.ratelimit_remaining)

    data = dict()
    # FIXME(BMo) don't save releases under the 'data' key
    # FIXME(BMo) extract document files from the release and save as
    #            list or dict in the data.
    data['repo'] = repository.as_dict()
    data['current'] = dict()
    data['current']['data'] = latest_release.as_dict()

    releases = repository.releases()
    for _release in releases:
        release_name = _release.name.replace(' ', '-')
        data[release_name] = dict()
        data[release_name]['data'] = _release.as_dict()

    # latest_release.archive(format='tarball')

    print('SAVING DATA')
    with open(data_file, 'wb') as _file:
        pickle.dump(data, _file, protocol=pickle.HIGHEST_PROTOCOL)
    return 'Updated'


def _load_data():
    """."""
    import pickle
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
            return data
    return None


@APP.route('/api/update')
def update_data():
    """Load or update data model from github api."""
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(query_github)
    message = async_result.get()
    return jsonify(dict(message='{} github data model'.format(message)))


@APP.route('/api/release/versions')
def api_release_versions():
    """."""
    import pickle
    import time
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        print('LOADING DATA')
        load_start = time.time()
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
        print('complete in {:4f} s'.format(time.time() - load_start))
        return jsonify(dict(versions=list(data.keys())))
    else:
        return jsonify(dict(error='data file not found! {}'.format(data_file)))


@APP.route('/api/release/all')
def api_release_all_dict():
    """."""
    import pickle
    import time
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        print('LOADING DATA')
        load_start = time.time()
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
        print('complete in {:4f} s'.format(time.time() - load_start))
        for version in data.keys():
            if 'data' in version:
                data[version]['data']['body'] = '**body**'
                data[version]['data']['body_html'] = '**body_html**'
                data[version]['data']['body_text'] = '**body_text**'
            if 'body' in version:
                data[version]['body'] = '**body**'
                data[version]['body_html'] = '**body_html**'
                data[version]['body_text'] = '**body_text**'
        return jsonify(data)
    else:
        return jsonify(dict(error='data file not found! {}'.format(data_file)))


@APP.route('/api/repo')
def api_repo_dict():
    """."""
    import pickle
    import time
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        print('LOADING DATA')
        load_start = time.time()
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
        print('complete in {:4f} s'.format(time.time() - load_start))
        return jsonify(data['repo'])
    else:
        return jsonify(dict(error='data file not found! {}'.format(data_file)))


@APP.route('/api/release/<version>')
def api_release_version_dict(version):
    """."""
    import pickle
    import time
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        print('LOADING DATA')
        load_start = time.time()
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
        print('complete in {:4f} s'.format(time.time() - load_start))
        if version not in data:
            jsonify(dict(error='version not found! {}'.format(data_file)))
        data = data[version]['data']
        data['body'] = '**body**'
        data['body_html'] = '**body_html**'
        data['body_text'] = '**body_text**'
        return jsonify(data)
    else:
        return jsonify(dict(error='data file not found! {}'.format(data_file)))


@APP.route('/api/release/<version>/body')
def api_release_version_body(version):
    """."""
    import pickle
    import time
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        print('LOADING DATA')
        load_start = time.time()
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
        print('complete in {:4f} s'.format(time.time() - load_start))
        if version not in data:
            jsonify(dict(error='version not found! {}'.format(data_file)))
        data = data[version]['data']
        return data['body_html']
    else:
        return jsonify(dict(error='data file not found! {}'.format(data_file)))


@APP.route('/api/release/<version>/docs')
def api_release_version_docs(version):
    """."""
    import pickle
    import time
    from bs4 import BeautifulSoup
    data_file = 'oskar_github_meta.pickle'
    if os.path.exists('oskar_github_meta.pickle'):
        print('LOADING DATA')
        load_start = time.time()
        with open(data_file, 'rb') as _file:
            data = pickle.load(_file)
        print('complete in {:4f} s'.format(time.time() - load_start))
        if version not in data:
            jsonify(dict(error='version not found! {}'.format(data_file)))
        data = data[version]['data']
        body_html = data['body_html']
        soup = BeautifulSoup(body_html, "html.parser")
        docs = []
        for link in soup.findAll('a'):
            _href = link.get('href')
            if '.pdf' in _href:
                name = _href.split('/')[-1]
                docs.append((name, _href))
        return jsonify(dict(docs=docs))
    else:
        return jsonify(dict(error='data file not found! {}'.format(data_file)))


@APP.route('/')
def home():
    """Homepage."""
    data = _load_data()
    return render_template('home.html.j2', data=data)


@APP.route('/faq')
def faq():
    """Frequency asked questions."""
    data = _load_data()
    return render_template('faq.html', data=data)


@APP.route('/downloads')
def downloads():
    """Downloads."""
    data = _load_data()
    return render_template('downloads.html', data=data)


@APP.route('/downloads/<version>')
def release(version):
    """Download a specified version."""
    data = _load_data()
    if version not in data.keys():
        return 'NOT FOUND'
    return render_template('release.html.j2', data=data, version=version)


@APP.route('/downloads/latest')
@APP.route('/downloads/current')
def latest_download():
    """."""
    data = _load_data()
    version = 'current'
    if version not in data.keys():
        return 'NOT FOUND'
    return render_template('release.html.j2', data=data, version=version)


@APP.route('/documentation')
def documentation():
    """Documentation."""
    data = _load_data()
    return render_template('documentation.html', data=data)


@APP.route('/quick_start')
@APP.route('/start')
def getting_start():
    """Display the getting started guide."""
    data = _load_data()
    return render_template('getting_started.html.j2', data=data)


@APP.route('/downloads/telescopes')
def telescope_models():
    """Download telescope model data."""
    data = _load_data()
    return render_template('telescope_models.html', data=data)


@APP.route('/downloads/sky')
def sky_models():
    """Download sky model data."""
    data = _load_data()
    return render_template('sky_models.html', data=data)


@APP.route('/downloads/scripts')
def scripts():
    """Download simulation scripts."""
    data = _load_data()
    return render_template('scripts.html', data=data)


if __name__ == '__main__':
    APP.run(host='0.0.0.0')
