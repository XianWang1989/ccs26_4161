
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal, get_locale
from babel import Locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure supported locales
LANGUAGES = {'en': 'English', 'fr': 'French', 'de': 'German'}
app.config['BABEL_LANGUAGES'] = LANGUAGES.keys()

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:')
    submit = SubmitField('Submit')

# Define locale selection based on URL parameter
@babel.localeselector
def get_locale():
    return request.args.get('lang', 'en')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Access the number as a Decimal
        number_value = form.number.data
        locale = get_locale()

        # Format the number based on locale
        formatted_number = format_decimal(number_value, locale=locale)

        return render_template('result.html', 
                               formatted_number=formatted_number)

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
