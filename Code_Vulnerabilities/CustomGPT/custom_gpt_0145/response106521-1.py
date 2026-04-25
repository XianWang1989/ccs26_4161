
from flask import Flask, render_template, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define the supported locales
LANGUAGES = {'en': 'English', 'fr': 'French'}

@babel.localeselector
def get_locale():
    # Here you can implement more complex locale selection
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    number = DecimalField('Localized Number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Get the submitted number formatted according to the locale
        number_value = format_decimal(form.number.data)
        return f'Formatted Number: {number_value}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
