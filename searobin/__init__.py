import os

from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            )

    # Load the instance config if it exists
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    # Load the test config passed in to create_app
    else:
        app.config.from_mapping(test_config)

    # Make sure there's an instance folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # The classic hello page
    @app.route('/hello')
    def hello():
        return 'Hello, Everybody!'

    return app
