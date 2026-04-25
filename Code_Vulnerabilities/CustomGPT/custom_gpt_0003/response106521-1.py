
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

# A simple configuration for locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR', 'de_DE'], 'en_US')

class NumberForm(FlaskForm):
    number = DecimalField('Localized Number', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Accessing the raw input value
        number = form.number.data
        # Formatting the number according to the locale
        formatted_number = format_currency(number, 'USD', locale=get_locale())
        return f'Formatted number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
