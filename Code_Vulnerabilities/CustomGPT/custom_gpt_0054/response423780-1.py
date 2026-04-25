
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import InputRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not field.data or all(item == "" for item in field.data):
            raise ValidationError('You must enter at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()

    if form.validate_on_submit():
        # Process the valid data from form.mylist
        items = form.mylist.data
        flash(f'Success! You submitted: {items}')
        return 'Form submitted!'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
