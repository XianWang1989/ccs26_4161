
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        locale = get_locale()
        formatted_amount = format_currency(amount, 'USD', locale=locale)
        flash(f'Formatted Amount: {formatted_amount}')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
