
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField
from wtforms.validators import InputRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or all(item == '' for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        # Process the valid data from mylist
        items = form.mylist.data
        return f'Submitted items: {items}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
