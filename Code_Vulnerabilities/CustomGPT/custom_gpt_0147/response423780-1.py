
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

def at_least_one_item(form, field):
    if not any(field.data):
        raise ValidationError('You must enter at least one item.')

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)

    def validate_mylist(form, field):
        at_least_one_item(form, field)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process form data
        print(form.mylist.data)  # Here you can handle the submitted array
        return redirect(url_for('index'))  # Redirect after successful submission

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
