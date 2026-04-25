
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize Babel
babel = Babel(app)

@babel.localeselector
def get_locale():
    # You can use user preferences or other methods to select the locale
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class CurrencyForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CurrencyForm()
    if form.validate_on_submit():
        amount = form.amount.data
        # Format the currency according to the current locale
        localized_amount = format_currency(amount, 'USD', locale=get_locale())
        return f'The formatted amount is: {localized_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
