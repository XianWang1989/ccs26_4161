
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if not any(field.data):  # Check if at least one item is filled
            raise ValidationError('At least one item must be provided in the list.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        return "Form is valid!"
    return render_template('form.html', form=form)

@app.route('/')
def index():
    return render_template('form.html', form=MyForm())

if __name__ == '__main__':
    app.run(debug=True)
