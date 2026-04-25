
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, mylist):
        if not mylist.data or all(item == '' for item in mylist.data):
            raise ValidationError('At least one item is required in the list.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid data
        flash('Form submitted successfully with: {}'.format(form.mylist.data))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
