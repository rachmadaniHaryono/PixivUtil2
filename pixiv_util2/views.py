from urllib.parse import urlparse, parse_qs

from flask import request
from flask_admin import AdminIndexView, expose
import structlog

from pixiv_util2 import forms


log = structlog.getLogger(__name__)


class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        form = forms.AdminIndexForm(request.args)
        template_kwargs = {'form': form, 'entries': []}
        image_ids = []
        if form.image_ids.data:
            template_kwargs['image_ids'] = [x.strip() for x in form.image_ids.data.split(',') if x.strip()]
        elif form.url.data:
            template_kwargs['image_ids'] = parse_qs(urlparse(form.url.data).query)['illust_id']
        else:
            template_kwargs['image_ids'] = image_ids
        log.debug('template kwargs', image_ids=template_kwargs['image_ids'])
        return self.render('pixiv_util2/admin_index.html', **template_kwargs)
