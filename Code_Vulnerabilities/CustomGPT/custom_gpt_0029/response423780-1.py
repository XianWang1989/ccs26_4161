
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('You must provide at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the valid form data
        return 'Form submitted successfully!'
    return render_template('form_template.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
