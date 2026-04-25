
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'))
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item must be filled.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process your data here
        return "Form submitted successfully!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
