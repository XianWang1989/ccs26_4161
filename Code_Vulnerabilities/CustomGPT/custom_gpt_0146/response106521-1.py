
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set your available locales
locales = ['en_US', 'fr_FR']

@babel.localeselector
def get_locale():
    # You can use request.accept_languages to decide the locale
    return request.accept_languages.best_match(locales)

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Retrieve the amount entered
        amount = form.amount.data
        # Format the amount according to the current locale
        formatted_amount = format_currency(amount, 'USD', locale=get_locale())
        return f'The formatted amount is: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
