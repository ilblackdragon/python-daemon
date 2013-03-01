"""Setup for python-deamon package forker from:
    https://github.com/wwwjfy/python-daemon and https://github.com/serverdensity/python-daemon/
"""

import os
from setuptools import setup, find_packages

from pymisc import VERSION, PROJECT

def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''

META_DATA = dict(
    name = PROJECT,
    version = VERSION,
    description = read('DESCRIPTION'),
    long_description = read('README.markdown'),
    license='MIT',

    author = "Illia Polosukhin",
    author_email = "ilblackdragon@gmail.com",

    url = "https://github.com/ilblackdragon/python-deamon.git",

    packages = find_packages(),
    package_data = { '': PACKAGE_DATA, },

    install_requires = [ ],
)

if __name__ == "__main__":
    setup( **META_DATA )

