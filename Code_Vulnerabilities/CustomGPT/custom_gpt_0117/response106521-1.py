
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

locales = {
    'en': 'en_US',
    'fr': 'fr_FR',
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(locales.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_amount = None
    if form.validate_on_submit():
        # Format the number using the current locale
        formatted_amount = format_decimal(form.amount.data)
    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
