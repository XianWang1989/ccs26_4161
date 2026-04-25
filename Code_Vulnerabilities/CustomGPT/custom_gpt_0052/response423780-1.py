
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=0)

    def validate_mylist(form, field):
        if not field.data or all(item == '' for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the data
        return 'Form successfully validated!'
    return render_template('form.html', form=form)

@app.route('/')
def index():
    form = MyForm()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
