from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class BucketItemForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    post =  TextAreaField(u'Post', validators=[DataRequired(), Length(max=200)])