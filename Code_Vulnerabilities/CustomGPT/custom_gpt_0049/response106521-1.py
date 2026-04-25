
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
import locale

app = Flask(__name__)
babel = Babel(app)

# Configure your locales
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Change to desired default locale

@babel.localeselector
def get_locale():
    return request.accept_languages.best_matching(['en', 'fr', 'de'])  # Example locales

class NumberForm(FlaskForm):
    number = DecimalField('Number', places=2, validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Get number from form and format it based on locale
        number = form.number.data
        formatted_number = format_number(number)
        return render_template('result.html', formatted_number=formatted_number)
    return render_template('form.html', form=form)

def format_number(number):
    # Get the current locale
    current_locale = get_locale()
    locale.setlocale(locale.LC_ALL, current_locale)

    # Format the number
    return locale.currency(number)

if __name__ == '__main__':
    app.run(debug=True)
