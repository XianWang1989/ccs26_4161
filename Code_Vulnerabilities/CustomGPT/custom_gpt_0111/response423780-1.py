
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'))

    def validate_mylist(self, field):
        if not any(field.data):  # Check if at least one item exists
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)

    if request.method == 'POST' and form.validate():
        # Handle the valid form data
        return redirect(url_for('success'))

    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
