
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Items', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')
