
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])  # Add your supported locales here

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_amount = None
    if form.validate_on_submit():
        amount = form.amount.data
        locale = get_locale()
        formatted_amount = format_currency(amount, 'USD', locale=locale)  # Change currency as needed
    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
