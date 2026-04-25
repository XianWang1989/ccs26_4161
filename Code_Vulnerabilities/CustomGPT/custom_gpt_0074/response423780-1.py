
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        # Check if at least one item is filled in the list
        if not any(field.data):
            raise ValidationError('You must provide at least one item in the list.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm(request.form)

    if form.validate_on_submit():
        # Process the list as needed
        return "Form submitted successfully with: " + ', '.join(form.mylist.data)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
