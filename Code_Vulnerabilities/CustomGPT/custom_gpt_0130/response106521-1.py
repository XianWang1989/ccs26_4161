
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_babel import Babel, format_decimal
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
}

# User locale selection
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    number = DecimalField('Number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format number according to locale
        formatted_number = format_decimal(form.number.data, locale=get_locale())
        return f'The localized number is: {formatted_number}'

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
