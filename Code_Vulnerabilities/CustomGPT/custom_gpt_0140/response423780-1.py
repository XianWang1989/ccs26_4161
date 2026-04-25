
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Custom validator
def requires_at_least_one(form, field):
    if not field.data:
        raise ValidationError('At least one item is required.')

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Items', [DataRequired()]), min_entries=1)

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the valid data
        items = form.mylist.data
        return f"Received: {items}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
