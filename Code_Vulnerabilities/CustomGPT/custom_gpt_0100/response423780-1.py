
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or len(field.data) == 0:
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process the data
        items = form.mylist.data
        return f'You submitted: {items}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
