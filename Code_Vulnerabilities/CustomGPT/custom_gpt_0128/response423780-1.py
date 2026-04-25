
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, FormField, validators
from wtforms.validators import ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(self, field):
        if not any(field.data):
            raise ValidationError('At least one item must be provided.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyListForm()
    if form.validate_on_submit():
        # Process the validated data
        items = form.mylist.data
        return f'Success! Items: {items}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
