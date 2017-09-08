from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields.html5 import DateField


class EntryForm(Form):
    title = StringField(
        'Title',
        validators=[DataRequired()])
    date = DateField(
        'Date (MM/DD/YYYY)',
        format='%Y-%m-%d'
        )
    timespent = StringField(
        'Time spent',
        validators=[DataRequired()])
    what_learned = TextAreaField(
        "What did you learn?",
        validators=[DataRequired()])
    resources = TextAreaField(
        "Resources",
        validators=[DataRequired()])


