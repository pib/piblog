from flask_script import Manager
from . import app

manager = Manager(app)


def run():
    manager.run()
