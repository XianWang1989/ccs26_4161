
from flask import Flask, render_template_string, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FieldList, StringField, ValidationError
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class MyForm(FlaskForm):
    mylist = FieldList(StringField('Item', validators=[DataRequired()]), min_entries=1)

    def validate_mylist(form, field):
        if not field.data or all(not item for item in field.data):
            raise ValidationError('At least one item is required.')

@app.route('/doit', methods=['GET', 'POST'])
def doit():
    form = MyForm()

    if form.validate_on_submit():
        # Process the data
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('doit'))

    return render_template_string('''
    <form method="post" action="/doit">
        {{ form.hidden_tag() }}
        {{ form.mylist(0) }} <br>
        {{ form.mylist(1) }} <br>
        {{ form.mylist(2) }} <br>
        {{ form.mylist(3) }} <br>
        <input type="submit" value="Submit">
    </form>
    {% for field in form.mylist %}
        {% for error in field.errors %}
            <span style="color: red;">{{ error }}</span><br>
        {% endfor %}
    {% endfor %}
    ''')

if __name__ == '__main__':
    app.run(debug=True)
