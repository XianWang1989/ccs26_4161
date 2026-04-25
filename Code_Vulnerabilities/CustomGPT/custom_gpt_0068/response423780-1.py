
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not field.data or all(item.data == "" for item in field.entries):
            raise ValidationError('You must provide at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()

    if form.validate_on_submit():
        # Process the valid form data
        items = [item.data for item in form.mylist if item.data]
        flash(f'Items submitted: {items}')
        return redirect(url_for('doit'))  # Redirect after submission

    return render_template('form.html', form=form)

@app.route('/')
def index():
    return redirect(url_for('doit'))

if __name__ == '__main__':
    app.run(debug=True)
