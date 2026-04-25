
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]))

    def validate_mylist(form, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError('You must provide at least one item.')

### Step 3: Define the Routes

Create a route to display the form and handle form submission.

