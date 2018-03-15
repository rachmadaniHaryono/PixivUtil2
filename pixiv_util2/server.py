"""Server module."""
import os
import sys

from flask import Flask, send_from_directory
from flask.cli import FlaskGroup
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import click
import structlog

from pixiv_util2 import views, models


log = structlog.getLogger(__name__)

if sys.version_info[0] < 3:
    print('PixivUtil2-server can only be run on 3')
    sys.exit(1)


def create_app(script_info=None):
    """create app."""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('PIXIVUTIL2_SERVER_SECRET_KEY') or os.urandom(24)
    app.config['DATABASE_FILE'] = 'pixiv_util2_server.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
    log.debug('sqlalchemy database', uri=app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    models.db.init_app(app)
    app.app_context().push()
    models.db.create_all()
    log.info('file path', v=models.file_path)
    try:
        os.mkdir(models.file_path)
    except OSError:
        pass

    @app.shell_context_processor
    def shell_context():
        return {'app': app, 'db': models.db}

    admin = Admin(
        app, name='PixivUtil2', template_mode='bootstrap3',
        index_view=views.HomeView(
            name='Home', template='pixiv_util2/admin_index.html', url='/'
        )
    )
    admin.add_view(views.ImageView(models.Image, models.db.session))
    model_args = [
        models.ImageUrl,
        models.Artist,
        models.Namespace,
        models.Tag,
        models.ImageId,
    ]
    for m in model_args:
        admin.add_view(ModelView(m, models.db.session))
    app.add_url_rule('/f/<path:filename>', 'files', lambda filename:send_from_directory(models.file_path, filename))  # NOQA
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    """This is a management script for application."""
    pass


if __name__ == '__main__':
    cli()
