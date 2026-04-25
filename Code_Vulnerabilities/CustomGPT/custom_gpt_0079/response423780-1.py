
from flask import Flask, render_template_string, request
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, SubmitField, ValidationError

app = Flask(__name__)
app.secret_key = 'secret'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item'))
    submit = SubmitField('Submit')

    def validate_mylist(form, field):
        if not any(field.data):  # Check if at least one item is given
            raise ValidationError('You must enter at least one item.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        return f'Success! You submitted: {form.mylist.data}'

    return render_template_string('''
    <form method="post">
        {{ form.mylist(placeholder="Enter item") }}
        {{ form.mylist(placeholder="Enter item") }}
        {{ form.mylist(placeholder="Enter item") }}
        {{ form.mylist(placeholder="Enter item") }}
        <input type="submit" value="Submit">
    </form>
    {{ form.mylist.errors }}
    ''')

if __name__ == '__main__':
    app.run(debug=True)
