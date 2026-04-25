
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import InputRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]))
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process your data here
        return "Form submitted successfully!"
    return render_template('form_template.html', form=form)

if __name__ == "__main__":
    app.run()
