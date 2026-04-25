
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not field.data or all(item == '' for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        return 'Form submitted successfully with: {}'.format(form.mylist.data)
    return render_template('form.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
