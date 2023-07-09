import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY= 'mykey',
    )

    from . import calculator

    app.register_blueprint(calculator.bp)

    return app