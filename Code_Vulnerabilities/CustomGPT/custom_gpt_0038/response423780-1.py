
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not any(field.data):  # Check if at least one item is provided
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the valid form data
        items = form.mylist.data
        flash(f'Success! You submitted: {items}')
        return redirect('/')  # Redirect after POST

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
