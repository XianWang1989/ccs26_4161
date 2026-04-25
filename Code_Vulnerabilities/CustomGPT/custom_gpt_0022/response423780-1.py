
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'))
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Process the valid data
        return 'Form submitted successfully with data: {}'.format(form.mylist.data)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
