from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, DateField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)
from wtforms.fields.html5 import DateField



class EntryForm(Form):
    title = StringField(
        'Title',
        validators=[DataRequired()])
    date = DateField(
        'Date (MM/DD/YYYY)',
        format='%Y-%m-%d'
        )
        # Need a regexp validator also
    timespent = StringField(
        'Time spent',
        validators=[DataRequired()])
    what_learned = TextAreaField(
        "What did you learn?",
        validators=[DataRequired()])
    resources = TextAreaField(
        "Resources",
        validators=[DataRequired()])


