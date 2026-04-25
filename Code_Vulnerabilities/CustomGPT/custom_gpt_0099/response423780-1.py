
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, Optional

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[Optional()]), min_entries=1)
    submit = SubmitField('Submit')
