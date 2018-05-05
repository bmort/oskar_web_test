# -*- coding: utf-8 -*-
"""

Consider:
<https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/>
"""

import os
import shutil
from distutils.dir_util import copy_tree
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

def main():
    """."""
    output_path = 'static_site'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    env = Environment(
        loader=PackageLoader('oskar_web', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('home.html')
    config=dict(new_release=True)
    html = template.render(**config)

    f = open(os.path.join(output_path, 'index.html'), 'w')
    f.write(html)

    for folder in ['static', 'assets']:
        copy_tree(os.path.join('oskar_web', folder),
                  os.path.join(output_path, folder))



if __name__ == '__main__':
    main()
