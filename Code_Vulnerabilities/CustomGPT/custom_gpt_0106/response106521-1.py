
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from babel.numbers import format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    number = DecimalField(_('Number'), validators=[DataRequired()])
    submit = SubmitField(_('Submit'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on the current locale
        formatted_number = format_decimal(form.number.data, locale=get_locale())
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
