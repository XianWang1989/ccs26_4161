
from flask import Flask, render_template, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, StopValidation

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ArrayField(FieldList):
    def __init__(self, item_field, min_entries=1, *args, **kwargs):
        super().__init__(item_field, *args, **kwargs)
        self.min_entries = min_entries

    def validate(self, form, extra_validators=()):
        if not super().validate(form, extra_validators):
            return False
        if len(self.entries) < self.min_entries:
            raise StopValidation('At least one item is required.')
        return True

class MyForm(FlaskForm):
    mylist = ArrayField(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        flash('Form submitted successfully with: ' + ', '.join([field.data for field in form.mylist]))
        return redirect('/doit')
    return render_template('form.html', form=form)

@app.route('/')
def index():
    return redirect('/doit')

if __name__ == '__main__':
    app.run(debug=True)
