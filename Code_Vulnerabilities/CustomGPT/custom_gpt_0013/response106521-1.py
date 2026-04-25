
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_babel import Babel, format_currency
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Sample language settings
LANGUAGES = {
    'en': 'English',
    'fr': 'French'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on the locale
        formatted_amount = format_currency(form.amount.data, 'USD', locale=get_locale())
        return f'The formatted amount is: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
