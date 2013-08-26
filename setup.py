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
        'Flask-Script',
        'Flask-Themes',
        'Frozen-Flask',
    ],

    entry_points={
        'console_scripts': [
            'piblog = piblog.script:run'
        ]
    }
)
