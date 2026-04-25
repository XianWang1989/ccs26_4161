
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not any(field.data):  # Check if at least one item is filled
            raise ValidationError('You must provide at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm()
    if form.validate_on_submit():
        # Process data
        items = form.mylist.data
        return f"Received items: {items}"

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
