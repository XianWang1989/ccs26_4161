
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection


class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or all(item == '' for item in field.data):
            raise ValidationError('You must enter at least one item.')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process form data, e.g., save to database or perform actions
        return redirect(url_for('success'))

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
