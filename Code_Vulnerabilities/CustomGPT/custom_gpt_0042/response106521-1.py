
from flask import Flask, render_template
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Dummy configuration for locales
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    return 'fr'  # Change this to dynamically get the user's locale

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_amount = None

    if form.validate_on_submit():
        formatted_amount = format_currency(form.amount.data, 'EUR')  # Change to desired currency

    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
