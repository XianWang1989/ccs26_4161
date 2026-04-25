
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, validators
from wtforms.validators import ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class CustomForm(FlaskForm):
    mylist = FieldList(StringField('Item', [validators.Optional()]), min_entries=1)

    # Custom validator to check that at least one item is present
    def validate_mylist(form, field):
        if not any(field.data):
            raise ValidationError('At least one item must be provided.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CustomForm()

    if form.validate_on_submit():
        # Process the valid form data
        items = form.mylist.data
        return f"Received items: {items}"

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
