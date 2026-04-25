
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ArrayField(FieldList):
    def __init__(self, *args, **kwargs):
        super().__init__(StringField(validators=[Length(min=1)]), *args, **kwargs)

    def validate(self, form, extra_validators=None):
        if len(self.entries) < 1:
            raise ValidationError('At least one item is required.')
        return super().validate(form, extra_validators)

class MyForm(FlaskForm):
    mylist = ArrayField()

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return "Form successfully submitted!"

if __name__ == '__main__':
    app.run(debug=True)
