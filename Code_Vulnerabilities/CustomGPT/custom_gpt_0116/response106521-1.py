
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, gettext as _
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Defining supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch'
}

@app.route('/set_language/<language>')
def set_language(language):
    # Set the locale for the session
    session['lang'] = language
    return redirect(url_for('index'))

@babel.localeselector
def get_locale():
    # Get the language from session
    return session.get('lang', 'en')

class NumberForm(FlaskForm):
    amount = DecimalField(_('Amount'), validators=[DataRequired()], places=2)
    submit = SubmitField(_('Submit'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()

    if form.validate_on_submit():
        amount = form.amount.data
        # Process the amount as necessary
        return redirect(url_for('index'))

    # Formatting the numbers based on the selected locale
    locale.setlocale(locale.LC_ALL, get_locale())
    formatted_amount = locale.format_string('%.2f', 1234.56, grouping=True)

    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
