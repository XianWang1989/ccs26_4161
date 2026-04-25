
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not any(field_list.data for field_list in field):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process your data here
        return 'Form submitted successfully! Items: ' + ', '.join([item for item in form.mylist.data])
    return render_template('form.html', form=form)

@app.route('/')
def index():
    form = MyListForm()
    return render_template('form.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
