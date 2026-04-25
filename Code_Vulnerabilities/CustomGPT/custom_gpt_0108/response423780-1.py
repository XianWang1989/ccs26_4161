
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not field.data or all(item.data == '' for item in field.data):
            raise ValidationError('You must enter at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid form data
        items = [item.data for item in form.mylist]
        return f'Submitted items: {items}'
    return render_template('form.html', form=form)

@app.route('/')
def index():
    form = MyForm()
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
