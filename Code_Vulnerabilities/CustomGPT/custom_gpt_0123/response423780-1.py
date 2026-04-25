
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or not any(field.data):
            raise ValidationError('You must provide at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm(request.form)

    if request.method == 'POST' and form.validate():
        # Process the valid data
        return redirect(url_for('success'))

    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
