
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(form, field):
        if not field.data:
            raise ValidationError('You must enter at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the data
        items = form.mylist.data
        return f"Received: {items}"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
