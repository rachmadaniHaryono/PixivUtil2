import os
import os.path as op

from appdirs import user_data_dir
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listens_for
from flask_admin import form


db = SQLAlchemy()
file_path = os.path.join(user_data_dir('pixiv_util2', 'nandaka'), 'files')


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    path = db.Column(db.String())
    checksum = db.Column(db.String())

    def __str__(self):
        return self.name


@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass
        # Delete thumbnail
        try:
            os.remove(op.join(file_path, form.thumbgen_filename(target.path)))
        except OSError:
            pass
