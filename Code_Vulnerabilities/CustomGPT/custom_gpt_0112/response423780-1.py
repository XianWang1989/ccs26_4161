
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Optional

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[Optional()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, mylist):
        if not any(mylist.data):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        return f'Success! Items: {items}'

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
