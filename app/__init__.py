# register blue-prints here
import os
from flask import Flask
from config import app_config  # local import


def create_app(config_name):
    app = Flask(__name__, static_folder=None)
    app_settings = os.getenv(
        'APP_SETTINGS',
        'config.DevelopmentConfig'
    )
    app.config.from_object(app_settings)

    return app




