
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]))
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if all(item.data == '' for item in field):
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return 'Form submitted successfully with items: ' + ', '.join(item.data for item in form.mylist)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
