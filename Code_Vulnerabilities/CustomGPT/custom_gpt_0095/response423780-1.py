
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', [DataRequired()]))

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return 'Form submitted successfully: ' + ', '.join(form.mylist.data)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
