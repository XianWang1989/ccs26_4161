
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if len(field.data) < 1:
            raise ValidationError('You must enter at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)

    if request.method == 'POST' and form.validate():
        # Process the valid input
        # Here you can access form.mylist.data, which is a list of input values
        return redirect(url_for('success'))

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
