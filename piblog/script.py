from flask_script import Manager
from . import create_app


def run():
    manager = Manager(create_app)
    manager.add_option(
        '-c', '--config', dest='config', required=False, default='piblog.cfg',
        help='Specify an alternative config file (default: "piblog.cfg")')
    manager.add_option(
        '-i', '--instance-path', dest='instance_path', required=False,
        default='.', help='Path containing site config (default: ".")')
    manager.run()
