
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MultiInputForm(FlaskForm):
    mylist = FieldList(StringField('Item'))
    submit = SubmitField('Submit')

    def validate_mylist(self, field):
        if not any(field.data):  # Check if at least one is filled
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MultiInputForm()

    if form.validate_on_submit():
        # Process the input if valid
        items = form.mylist.entries
        items_data = [item.data for item in items if item.data]
        flash(f'Success! Items: {items_data}')
        return render_template('success.html', items=items_data)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
