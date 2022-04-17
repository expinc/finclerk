import click
import os
# from . import auth
# from . import blog
from . import db
from flask import Flask
from flask.cli import with_appcontext

@click.command('init-schema')
@with_appcontext
def init_schema_command():
    """Clear the existing data and create new tables."""
    db.init_schema()
    click.echo('Initialized the database schema.')

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, 'finclerk.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.cli.add_command(init_schema_command)

    # TODO: register blueprints
    # app.add_url_rule('/', endpoint='index')

    return app
