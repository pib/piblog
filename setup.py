from setuptools import setup, find_packages

setup(
    name='piblog',
    version='0.1',
    url='http://probablyprogramming.com/',
    author='Paul Bonser',
    author_email='pib@paulbonser.com',
    description='Static blog generator',

    packages=['piblog'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Assets',
        'Flask-FlatPages',
        'Flask-Fleem',
        'Flask-Script',
        'Frozen-Flask',
        'Pygments',
    ],
    extras_require={
        'debug': ['Flask-DebugToolbar']
    },
    dependency_links=[
        'git+https://github.com/thrisp/fleem.git@b233dcf5a2#egg=flask_fleem-0.0.3'
    ],


    entry_points={
        'console_scripts': [
            'piblog = piblog.script:run'
        ]
    }
)
