from flask import Flask, render_template
from app.config import config
from app.views import DEFAULT_BLUEPRINT, config_blueprint
from app.extensions import config_extensions


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    config_extensions(app)
    config_blueprint(app)
    config_errorhandle(app)
    return app


def config_errorhandle(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')
