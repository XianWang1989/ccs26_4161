
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    # Creating a list of string fields for 'mylist'
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if len(field.data) == 0:  # Check if mylist is empty
            raise ValidationError('You must provide at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Handle valid form submission
        items = form.mylist.data  # Get the submitted list of items
        # Process the items as needed
        return redirect('/success')  # Redirect after a successful submission
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
