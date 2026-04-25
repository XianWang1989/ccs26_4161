
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_amount = None

    if form.validate_on_submit():
        # Format the decimal based on the current locale
        amount = form.amount.data
        formatted_amount = format_currency(amount, 'USD', locale=get_locale())

    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
