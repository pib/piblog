from flask import Blueprint, Flask
from flask_fleem import Fleem, theme_manager
from flask_flatpages import FlatPages
from os.path import abspath, join

try:
    import flask_debugtoolbar as dbt  # pylint: disable=F0401
except ImportError:
    dbt = None

blueprint = Blueprint('blueprint', __name__)
pages = FlatPages()

from piblog.views import instance_theme_loader


def init_app(app):
    app.register_blueprint(blueprint)
    pages.init_app(app)
    Fleem(app, loaders=[instance_theme_loader,
                        theme_manager.packaged_themes_loader,
                        theme_manager.theme_paths_loader])
    if dbt is not None:
        dbt.DebugToolbarExtension(app)


def create_app(config=None, instance_path=None):
    if instance_path is not None:
        instance_path = abspath(instance_path)

    app = Flask(__name__, instance_path=instance_path,
                instance_relative_config=True)

    if config is not None:
        app.config.from_pyfile(config)
        app.config.setdefault('FLATPAGES_ROOT',
                              join(app.instance_path, 'posts'))
        app.config.setdefault('FLATPAGES_EXTENSION', '.md')

    init_app(app)

    return app
