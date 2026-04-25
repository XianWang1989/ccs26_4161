
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ArrayField(FieldList):
    def __init__(self, *args, **kwargs):
        super().__init__(StringField(), *args, **kwargs)

    def validate(self, form, extra_validators=[]):
        if len(self.entries) < 1:
            raise ValidationError('At least one item is required.')
        return super().validate(form, extra_validators)

class MyForm(FlaskForm):
    mylist = ArrayField('My List', min_entries=1)

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)

    if request.method == 'POST' and form.validate():
        # Process the valid data
        return redirect(url_for('success'))

    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
