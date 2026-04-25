
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)  # Minimum one entry
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not field.data or all(item.strip() == '' for item in field.data):
            raise ValidationError('You must enter at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        # If form is valid, here you can process your mylist data
        items = form.mylist.data
        print("Received items:", items)
        return redirect(url_for('success'))  # Redirect after successful submission

    return render_template('form.html', form=form)

@app.route('/')
def home():
    form = MyForm()
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return '<h1>Form submitted successfully!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
