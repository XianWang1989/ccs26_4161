
from flask import Flask, render_template, request
from flask_babel import Babel, format_locale
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import babel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Sample available locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch',
}

# Set the default locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Here, you can handle the submitted data
        # You may want to format the number based on the current locale
        formatted_number = babel.numbers.format_decimal(form.number.data, locale=get_locale())
        return f'Formatted Number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
