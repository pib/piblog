from flask_script import Manager
from . import create_app


def run():
    manager = Manager(create_app)
    manager.add_option('-c', '--config', dest='config', required=False,
                       help='Specify a config to load before running')
    manager.run()
