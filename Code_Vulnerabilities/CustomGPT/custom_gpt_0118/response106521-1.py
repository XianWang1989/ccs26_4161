
from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_currency

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define supported locales
SUPPORTED_LOCALES = ['en_US', 'fr_FR']
app.config['BABEL_DEFAULT_LOCALE'] = 'en_US'

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(SUPPORTED_LOCALES)

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        # Format the amount according to the current locale
        formatted_amount = format_currency(amount, currency='USD')
        flash(f'Formatted amount: {formatted_amount}')
        return redirect('/')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
