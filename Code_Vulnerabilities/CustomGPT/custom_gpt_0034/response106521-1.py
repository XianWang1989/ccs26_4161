
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

babel = Babel(app)

# Configure available locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number according to the current locale
        formatted_amount = format_number(form.amount.data)
        return f'Formatted Amount: {formatted_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
