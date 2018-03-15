from datetime import datetime
import os
import os.path as op

from appdirs import user_data_dir
from flask_admin import form
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listens_for
from sqlalchemy.types import TIMESTAMP
from sqlalchemy_utils.types import URLType


db = SQLAlchemy()
file_path = os.path.join(user_data_dir('pixiv_util2', 'nandaka'), 'files')
image_id_tags = db.Table(
    'image_id_tags',
    db.Column('image_id', db.Integer, db.ForeignKey('image_id.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(TIMESTAMP, default=datetime.utcnow, nullable=False)


class Image(Base):
    name = db.Column(db.String)
    path = db.Column(db.String)
    checksum = db.Column(db.String)

    def __str__(self):
        return self.name


class ImageUrl(Base):
    value = db.Column(URLType)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    image = db.relationship(
        'Image', foreign_keys='ImageUrl.image_id', lazy='subquery',
        backref=db.backref('image_urls', lazy=True))


class Artist(Base):
    avatar_id = db.Column(db.Integer, db.ForeignKey('image_url.id'))
    avatar = db.relationship(
        'ImageUrl', foreign_keys='Artist.avatar_id', lazy='subquery',
        backref=db.backref('artists', lazy=True))
    artist_id = db.Column(db.Integer)
    name = db.Column(db.String)
    token = db.Column(db.String)
    # haveImages
    # isLastPage


class Namespace(Base):
    value = db.Column(db.String)


class Tag(Base):
    name = db.Column(db.String)
    namespace_id = db.Column(db.Integer, db.ForeignKey('namespace.id'))
    namespace = db.relationship(
        'Namespace', foreign_keys='Tag.namespace_id', lazy='subquery',
        backref=db.backref('tags', lazy=True))


class ImageId(Base):
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship(
        'Artist', foreign_keys='ImageId.artist_id', lazy='subquery',
        backref=db.backref('image_ids', lazy=True))
    # bookmark_count
    # dateFormat
    # descriptionUrlList
    # fromBookmark
    image_caption = db.Column(db.String)
    image_count = db.Column(db.Integer)
    image_mode = db.Column(db.String)
    image_title = db.Column(db.String)
    image_urls = None  # TODO
    jd_rtc = db.Column(db.Integer)
    jd_rtv = db.Column(db.Integer)
    original_artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship(
        'Artist', foreign_keys='ImageId.original_artist_id', lazy='subquery',
        backref=db.backref('image_ids', lazy=True))
    works_date = db.Column(db.String)
    works_date_date_time = db.Column(db.DateTime)
    # worksResolution  # split into 'width' and 'height'

    # value not from original PixivUtil2
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    value = db.Column(db.Integer)  # aka imageId
    #
    image_tags = db.relationship(
        'Tag', secondary=image_id_tags, lazy='subquery',
        backref=db.backref('image_ids', lazy=True))


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
