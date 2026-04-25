
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'))
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(field.data):  # Check if any input is filled
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if form.validate_on_submit():
        # Process the valid mylist
        data = form.mylist.data
        return f'You submitted: {data}'

    return render_template('my_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
