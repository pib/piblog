from . import blueprint, pages
from flask import current_app, g
from flask_fleem import render_theme_template
from flask_fleem.theme_manager import load_themes_from
import os.path


@blueprint.route('/')
def index():
    posts = [page for page in pages if 'published' in page.meta]
    sorted_posts = sorted(posts, reverse=True,
                          key=lambda page: page.meta['published'])
    return render_theme_template(get_current_theme(), 'index.html',
                                 posts=sorted_posts)


@blueprint.route('/<path:path>/')
def post(path):
    page = pages.get_or_404(path)
    return render_theme_template(get_current_theme(), 'post.html', post=page)


def get_current_theme():
    try:
        return g.user.theme
    except AttributeError:
        return current_app.config.get('DEFAULT_THEME', 'plain')


def instance_theme_loader(app):
    themes_dir = os.path.join(app.instance_path, 'themes')
    if os.path.isdir(themes_dir):
        return load_themes_from(themes_dir)
    else:
        return ()
