from flask import Blueprint, Flask, current_app

piblog_bp = Blueprint('piblog_bp', __name__)


@piblog_bp.route('/')
def index():
    configured_message = current_app.config.get('INDEX_MESSAGE',
                                                'Simple Index')
    return '<html><head></head><body>{}</body></html>'.format(
        configured_message)


def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(piblog_bp)

    if config is not None:
        app.config.from_pyfile(config)

    return app
