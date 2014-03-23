from flask_fleem import get_themes_list
from flask_frozen import walk_directory


def theme_static():
    for theme in get_themes_list():

        for static_file in walk_directory(theme.static_path):
            yield ('_themes.static', {'themeid': theme.identifier,
                                      'filename': static_file})
