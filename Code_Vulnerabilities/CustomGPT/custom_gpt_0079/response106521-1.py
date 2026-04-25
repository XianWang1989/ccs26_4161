
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from babel.numbers import format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define supported locales
SUPPORTED_LOCALES = ['en', 'fr', 'de']

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(SUPPORTED_LOCALES)

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = None

    if form.validate_on_submit():
        # Format the number based on the current locale
        number = form.amount.data
        formatted_number = format_decimal(number, locale=get_locale())

    return render_template('index.html', form=form, formatted_number=formatted_number)

if __name__ == '__main__':
    app.run(debug=True)
