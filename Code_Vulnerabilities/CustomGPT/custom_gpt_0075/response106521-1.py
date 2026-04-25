
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency, _get_locale
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define supported locales
LOCALES = ['en_US', 'fr_FR']  # Add more as needed

@babel.localeselector
def get_locale():
    return _get_locale() or request.accept_languages.best_match(LOCALES)

class NumberForm(FlaskForm):
    amount = DecimalField('Enter amount', format="%.2f")
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        formatted_amount = format_currency(amount, 'USD', locale=get_locale())
        return f'Formatted Amount: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
