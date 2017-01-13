from flask_wtf import Form
from wtforms import TextField, TextAreaField, BooleanField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo




class BucketItemForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description =  TextAreaField(u'Description', validators=[DataRequired(), Length(max=200)])
    validators = [FileAllowed(['jpg'], message='Must be a jpg file!')]
    photo = FileField('Photos', validators=validators)
    private = BooleanField('Mark as Private')
    done = BooleanField('Mark as Done')