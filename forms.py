from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)



class EntryForm(Form):
    title = StringField(
        'Title',
        validators=[DataRequired()])
    timespent = StringField(
        'Time spent',
        validators=[DataRequired()])
    what_learned = TextAreaField(
        "What did you learn?",
        validators=[DataRequired()])
    resources = TextAreaField(
        "Resources",
        validators=[DataRequired()])


