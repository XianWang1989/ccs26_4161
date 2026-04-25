
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]))

    def validate_mylist(form, field):
        if not any(field.data):  # Check if at least one item is filled
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        # Do something with the items...
        return redirect(url_for('success'))  # Redirect after processing
    return render_template('your_template.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
