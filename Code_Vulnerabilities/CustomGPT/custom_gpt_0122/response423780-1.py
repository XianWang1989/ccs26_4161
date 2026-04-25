
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[Length(min=1)]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, mylist):
        if not any(item.data for item in mylist):
            raise ValidationError('You must enter at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid data
        items = form.mylist.data
        return redirect(url_for('success', items=items))

    return render_template('form.html', form=form)

@app.route('/success')
def success():
    # Display results
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
