"""Server module."""
import os
import sys

from flask import Flask
from flask.cli import FlaskGroup
from flask_admin import Admin
import click
import structlog

from pixiv_util2 import views


log = structlog.getLogger(__name__)

if sys.version_info[0] < 3:
    print('PixivUtil2-server can only be run on 3')
    sys.exit(1)


def create_app(script_info=None):
    """create app."""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('PIXIVUTIL2_SERVER_SECRET_KEY') or os.urandom(24)

    @app.shell_context_processor
    def shell_context():
        # return {'app': app, 'db': models.db}
        return {'app': app}

    Admin(
        app, name='PixivUtil2', template_mode='bootstrap3',
        index_view=views.HomeView(
            name='Home', template='pixiv_util2/admin_index.html', url='/'
        )
    )
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """This is a management script for application."""
    pass


if __name__ == '__main__':
    cli()
