
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français'
}

@babel.localeselector
def get_locale():
    # You can implement your locale selection logic here
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        localized_amount = format_currency(form.amount.data, 'USD', locale=get_locale())
        return f'Formatted Amount: {localized_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
