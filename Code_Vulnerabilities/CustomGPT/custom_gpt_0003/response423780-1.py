
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, FormField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

# Custom validator to check that at least one field is filled
def validate_non_empty_list(form, field):
    if not any(field.data):
        raise ValidationError('At least one item is required.')

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()], default=''))

class MainForm(FlaskForm):
    mylist = FieldList(StringField(validators=[validate_non_empty_list]))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    if form.validate_on_submit():
        # Handle the submitted data
        items = form.mylist.data
        flash(f'Submitted items: {items}', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

