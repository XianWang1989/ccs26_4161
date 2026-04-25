
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]))

    def validate_mylist(form, field):
        if not any(field.data):  # Check if at least one item is filled
            raise ValidationError('You must enter at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the data
        items = form.mylist.data
        return f"Received: {items}"
    return render_template('form.html', form=form)

@app.route('/')
def index():
    form = MyForm()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
