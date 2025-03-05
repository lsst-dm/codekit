#!/usr/bin/env python3
"""Setup Tools Script"""
import codecs
import os

from setuptools import find_packages, setup

PACKAGENAME = 'sqre-codekit'
DESCRIPTION = 'LSST Data Management SQuaRE code management tools'
AUTHOR = 'Frossie Economou'
AUTHOR_EMAIL = 'frossie@lsst.org'
URL = 'https://github.com/lsst-sqre/sqre-codekit'
LICENSE = 'MIT'


def read(filename):
    """Convenience function for includes"""
    full_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
    return codecs.open(full_filename, 'r', 'utf-8').read()


long_description = read('README.md')  # pylint:disable=invalid-name

setup(
    name=PACKAGENAME,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='lsst',
    use_scm_version=True,
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'MapGitConfig',
        'progressbar2',
        'public',
        'pygithub',
        'pyyaml',
        'requests',
    ],
    setup_requires=[
        'pytest-runner',
        'setuptools_scm',
    ],
    tests_require=[
        'flake8',
        'pytest',
        # Removed due to incompatibility
        # 'pytest-flake8',
        'responses',
    ],
    # package_data={},
    entry_points={
        'console_scripts': [
            'github-auth = codekit.cli.github_auth:main',
            'github-decimate-org = codekit.cli.github_decimate_org:main',
            'github-fork-org = codekit.cli.github_fork_org:main',
            'github-get-ratelimit= codekit.cli.github_get_ratelimit:main',
            'github-list-repos = codekit.cli.github_list_repos:main',
            'github-mv-repos-to-team = codekit.cli.github_mv_repos_to_team:main',  # NOQA
            'github-tag-release = codekit.cli.github_tag_release:main',
            'github-tag-teams = codekit.cli.github_tag_teams:main',
        ]
    },
)
