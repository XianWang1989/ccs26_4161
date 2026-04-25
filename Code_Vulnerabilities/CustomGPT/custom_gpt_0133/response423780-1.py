
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to your actual secret key!

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(form, field):
        # Custom validation to ensure at least one item is present
        if not any(field.data):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process the validated data
        items = form.mylist.data
        return redirect(url_for('success', items=items))

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    items = request.args.getlist('items')
    return f'Success! You submitted: {", ".join(items)}'

if __name__ == '__main__':
    app.run(debug=True)
