"""
STUFF
"""
from setuptools import setup


__name__ = "FooBar"
__version__ = "0.0.1-dev"
__author__ = "Innovation Team"
__email__ = "innovation@ebpi.nl"

setup(
    name = __name__,
    version = __version__,
    author = __author__,
    author_email = __email__,
    license = __license__,
    description = __doc__.splitlines()[0],
    long_description = open('README.rst').read(),
    url = 'http://github.com/mhogerheijde/jira-git',
    download_url = 'http://github.com/mhogerheijde/jira-git/archives/master',
    packages = ['jira-git'],
    include_package_data = True,
    zip_safe = False,
    platforms = ['all'],
    test_suite = 'tests',
    entry_points = {
    },
    install_requires = [
        'requests',
        # 'rsa',
        # 'suds',
    ],
)
