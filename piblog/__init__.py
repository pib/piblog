from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<html><head></head><body>Simple index</body></html>'
