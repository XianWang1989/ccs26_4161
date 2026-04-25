
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, get_locale
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up some locales for demonstration
locales = {
    'en': 'en_US.UTF-8',
    'fr': 'fr_FR.UTF-8',
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(locales.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the submitted number
        return f"Submitted amount: {locale.currency(form.amount.data, grouping=True)}"

    return render_template('index.html', form=form)

@app.context_processor
def inject_number_format():
    user_locale = get_locale()
    locale.setlocale(locale.LC_ALL, locales[user_locale])
    return {'locale_currency_format': locale.currency}

if __name__ == '__main__':
    app.run(debug=True)
