"""Forms module."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Optional


class AdminIndexForm(FlaskForm):
    """Form for index."""
    url = StringField('url', validators=[Optional])
    image_ids = StringField('image ids', validators=[Optional])
