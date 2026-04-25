
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for CSRF protection

class ListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, mylist):
        if not any(field.data for field in mylist):
            raise ValidationError('At least one item must be provided.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = ListForm()
    if form.validate_on_submit():
        # Process the valid data
        return "Form submitted successfully with data: {}".format(form.mylist.data)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
