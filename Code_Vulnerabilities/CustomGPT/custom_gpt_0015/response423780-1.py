
from flask import Flask, render_template_string, request
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, validators
from wtforms.validators import ValidationError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[validators.Optional()]), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or all(not item for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm(request.form)
    if request.method == 'POST' and form.validate():
        # Process the form data
        items = form.mylist.data
        return f"Submitted items: {items}"
    return render_template_string('''
        <form method="post" action="/doit">
            {{ form.mylist[0]() }}
            {{ form.mylist[1]() }}
            {{ form.mylist[2]() }}
            {{ form.mylist[3]() }}
            <input type="submit" value="Submit">
        </form>
        {% for error in form.mylist.errors %}
            <div style="color: red;">{{ error }}</div>
        {% endfor %}
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
