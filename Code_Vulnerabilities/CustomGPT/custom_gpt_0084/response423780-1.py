
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Custom validator to check if at least one field is filled
def at_least_one(form, field):
    if not any(form.mylist.data):
        raise ValidationError('At least one item is required.')

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1, max_entries=10, validators=[at_least_one])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        # Process the valid form data
        return redirect('/success')

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
