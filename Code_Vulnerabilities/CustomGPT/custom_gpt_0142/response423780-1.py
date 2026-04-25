
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, FormField
from wtforms.validators import DataRequired, Optional, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class ItemForm(FlaskForm):
    name = StringField('Item', validators=[DataRequired()])

class MyListForm(FlaskForm):
    items = FieldList(FormField(ItemForm), min_entries=1)  # Ensure at least one item

    def validate_items(form, field):
        if not any(form.items.data):
            raise ValidationError('You must provide at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm(request.form)

    if request.method == 'POST' and form.validate():
        # Process the data
        items = [item['name'] for item in form.items.data]
        # Do something with the validated items
        print(items)
        return redirect(url_for('doit'))

    return render_template('form.html', form=form)

@app.route('/')
def index():
    return redirect(url_for('doit'))

if __name__ == '__main__':
    app.run(debug=True)
