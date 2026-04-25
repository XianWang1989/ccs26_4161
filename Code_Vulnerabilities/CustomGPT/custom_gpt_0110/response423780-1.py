
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]))

    def validate_mylist(form, field):
        if len(field.data) == 0:
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid data, e.g., save to database
        return redirect(url_for('success'))

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
