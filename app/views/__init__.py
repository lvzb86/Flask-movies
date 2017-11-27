from .main import main
from .user import user
from .movie import movie

DEFAULT_BLUEPRINT = (
    (main, ''),
    (user, '/user'),
    (movie,'/movie')
)


def config_blueprint(app):
    for blue_print, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blue_print, url_prefix=url_prefix)
