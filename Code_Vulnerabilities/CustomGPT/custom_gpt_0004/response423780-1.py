
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]))

    def validate_mylist(self, mylist):
        if not mylist.data:
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        items = form.mylist.data
        return f"Submitted items: {items}"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
