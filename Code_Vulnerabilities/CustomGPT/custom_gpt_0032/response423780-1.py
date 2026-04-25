
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Field, ValidationError
from wtforms.fields import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ArrayField(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_formdata(self, valuelist):
        self.data = [value for value in valuelist if value]

    def pre_validate(self, form):
        if not self.data or len(self.data) == 0:
            raise ValidationError('At least one item is required.')

class MyForm(FlaskForm):
    mylist = ArrayField()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully with at least one item in mylist!"

if __name__ == '__main__':
    app.run(debug=True)
