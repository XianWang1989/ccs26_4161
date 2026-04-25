
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for CSRF protection

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not any(item.data for item in field):  # Check if at least one item is filled
            raise ValidationError('Please enter at least one item.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Process the valid data
        items = [item.data for item in form.mylist]
        return f'Valid items: {items}'

    return render_template('form_template.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
