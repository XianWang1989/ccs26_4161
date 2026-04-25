
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set the locale for number formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Change to the desired locale

class NumberForm(FlaskForm):
    number = DecimalField('Enter a Number:', places=2, validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Convert the submitted number to a locale-specific format
        formatted_number = locale.format_string('%.2f', form.number.data, grouping=True)
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
