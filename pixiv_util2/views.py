from urllib.parse import urlparse, parse_qs
import imghdr
import os
import tempfile

from flask import request, url_for
from flask_admin import AdminIndexView, expose, form
from flask_admin.contrib import sqla
from jinja2 import Markup
import hashlib
import structlog

from pixiv_util2 import forms, models as pu2_models
import PixivUtil2
import PixivDBManager
import PixivHelper
import PixivBrowserFactory

from . import models


log = structlog.getLogger(__name__)


def sha256_checksum(filename, block_size=65536):
    """sha256 checksum."""
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as file_path:
        for block in iter(lambda: file_path.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        index_form = forms.AdminIndexForm(request.args)
        template_kwargs = {'form': index_form, 'entries': []}
        if index_form.input_type.data == forms.AdminIndexForm.INPUT_TYPE_IMAGE_ID:
            template_kwargs['image_ids'] = [x.strip() for x in index_form.image_ids.data.split(',') if x.strip()]
        elif index_form.input_type.data == forms.AdminIndexForm.INPUT_TYPE_URL:
            template_kwargs['image_ids'] = parse_qs(urlparse(index_form.url.data).query)['illust_id']
        else:
            template_kwargs['image_ids'] = []
        if template_kwargs['image_ids']:
            try:
                PixivUtil2.__config__.loadConfig(path=PixivUtil2.configfile)
                PixivHelper.setConfig(PixivUtil2.__config__)
            except BaseException:
                print('Failed to read configuration.')
                log.exception('Failed to read configuration.')
            if PixivUtil2.__br__ is None:
                PixivUtil2.__br__ = PixivBrowserFactory.getBrowser(config=PixivUtil2.__config__)
            PixivUtil2.__dbManager__ = PixivDBManager.PixivDBManager(
                target=PixivUtil2.__config__.dbPath, config=PixivUtil2.__config__)
            PixivUtil2.__dbManager__.createDatabase()
            username = PixivUtil2.__config__.username
            password = PixivUtil2.__config__.password
            PixivUtil2.doLogin(password, username)
            PixivUtil2.start_iv = False
            for image_id in template_kwargs['image_ids']:
                PixivUtil2.process_image(None, int(image_id))
        log.debug('template kwargs', image_ids=template_kwargs['image_ids'])
        return self.render('pixiv_util2/admin_index.html', **template_kwargs)

def generate_image_name(obj, file_data):
    import shutil
    filename = file_data.filename
    filename_ext = os.path.splitext(filename)[1]
    with tempfile.NamedTemporaryFile() as temp:
        shutil.copyfileobj(file_data.stream._file, temp)
        imghdr_val = imghdr.what(temp.name)
        checksum = sha256_checksum(temp.name)

    filename_ext = '.' + imghdr_val if imghdr_val else filename_ext
    if filename_ext:
        new_filename = '{}{}'.format(checksum, filename_ext)
    else:
        new_filename = checksum
    new_filename = os.path.join(new_filename[:2], new_filename)
    file_data.filename = new_filename
    obj.checksum = checksum
    namespace = models.get_or_create(models.db.session, models.Namespace, value='filename')[0]
    tag = models.get_or_create(models.db.session, models.Tag, namespace=namespace, name=filename)[0]
    obj.tags.append(tag)
    models.db.session.add(obj)
    return new_filename


class ImageView(sqla.ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        return Markup('<a href="{1}"><img src="{0}"></a>'.format(
            url_for('files', filename=form.thumbgen_filename(model.path)),
            url_for('files', filename=model.path),
        ))

    column_formatters = {
        'path': _list_thumbnail
    }
    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'path': form.ImageUploadField(
            'Image', base_path=pu2_models.file_path, thumbnail_size=(100, 100, True), namegen=generate_image_name)
    }
