
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_number

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your locales (e.g., for French and English)
locales = {
    'en': 'en_US',
    'fr': 'fr_FR'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(locales.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        # Format the number based on the current locale
        formatted_number = format_number(amount, locale=get_locale())
        return f'Formatted number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
