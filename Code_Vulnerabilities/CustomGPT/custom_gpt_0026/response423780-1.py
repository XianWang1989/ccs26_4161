
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]),
                       min_entries=1)

    def validate_mylist(form, field):
        if not field.data:  # Check if the list is empty
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Handle the validated data here
        items = form.mylist.data
        return f'Success! You submitted: {items}'

    return render_template('form.html', form=form)

@app.route('/form')
def form_view():
    form = MyForm()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
