from flask_frozen import Freezer
from flask_script import Command, Manager
from . import create_app, generators


manager = Manager(create_app)

manager.add_option(
    '-c', '--config', dest='config', required=False, default='piblog.cfg',
    help='Specify an alternative config file (default: "piblog.cfg")')
manager.add_option(
    '-D', '--debug-toolbar', dest='debug_toolbar', action='store_true',
    default=False, help='Enable Flask-DebugToolbar if installed')
manager.add_option(
    '-i', '--instance-path', dest='instance_path', required=False,
    default='.', help='Path containing site config (default: ".")')


class FreezeCommand(Command):

    'Freeze the site to static files.'

    def handle(self, app):
        freezer = Freezer(app)
        freezer.register_generator(generators.theme_static)
        freezer.freeze()

manager.add_command('freeze', FreezeCommand())


def run():
    manager.run()
