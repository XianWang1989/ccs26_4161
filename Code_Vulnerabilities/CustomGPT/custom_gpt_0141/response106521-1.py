
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up the default locale
@app.before_request
def before_request():
    # You can set the user locale based on their preferences
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Change as needed

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', format='%0.2f')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = None
    if form.validate_on_submit():
        # Retrieve the raw number
        number = form.number.data

        # Format the number according to the current locale
        formatted_number = format_decimal(number, locale=locale.getlocale())

    return render_template('index.html', form=form, formatted_number=formatted_number)

if __name__ == "__main__":
    app.run(debug=True)
