
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm(request.form)

    if form.validate_on_submit():
        # Process the data
        items = form.mylist.data
        return f"Received: {items}"

    return render_template('form.html', form=form)

@app.route('/')
def index():
    return render_template('form.html', form=MyListForm())

if __name__ == '__main__':
    app.run(debug=True)
