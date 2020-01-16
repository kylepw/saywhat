from flask import Flask
import os


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # Default settings
        app.config.from_pyfile('settings.py')
    else:
        # Override with test settings
        app.config.from_mapping(test_config)

    from .views import main
    app.register_blueprint(main)

    return app