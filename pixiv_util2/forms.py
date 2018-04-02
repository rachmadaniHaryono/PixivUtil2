"""Forms module."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class AdminIndexForm(FlaskForm):
    """Form for index."""
    # INPUT_TYPE_DEFAULT = 0
    INPUT_TYPE_URL = 1
    INPUT_TYPE_IMAGE_ID = 2
    INPUT_TYPE_CHOICE = [
        (INPUT_TYPE_URL, 'URL'),
        (INPUT_TYPE_IMAGE_ID, 'Image id'),
    ]
    user_input = StringField('Input', validators=[DataRequired])
    input_type = SelectField('Type', choices=INPUT_TYPE_CHOICE)
