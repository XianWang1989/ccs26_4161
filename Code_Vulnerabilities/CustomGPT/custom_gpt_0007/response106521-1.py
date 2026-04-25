
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, validators
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set default locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Define your form
class NumberForm(FlaskForm):
    number = FloatField('Number', [validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NumberForm()
    if form.validate_on_submit():
        # Access the submitted number
        number = form.number.data
        # Format the number according to the current locale
        formatted_number = format_decimal(number, format='%.2f')
        return f'Formatted Number: {formatted_number}'

    return render_template('form.html', form=form)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

if __name__ == '__main__':
    app.run(debug=True)
