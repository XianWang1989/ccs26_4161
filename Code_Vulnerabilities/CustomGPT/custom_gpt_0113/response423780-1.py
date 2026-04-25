
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyListForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[InputRequired()]), min_entries=1)

    def validate_mylist(self, field):
        if not field.data:
            raise ValidationError('At least one item is required.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyListForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the valid list
        return redirect(url_for('success'))

    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
