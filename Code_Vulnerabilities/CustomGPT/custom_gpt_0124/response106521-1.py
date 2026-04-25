
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configuring supported locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class MyForm(FlaskForm):
    amount = DecimalField('Amount', places=2, rounding=None)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        amount = form.amount.data
        # Format the amount based on the current locale
        formatted_amount = format_currency(amount, 'USD', locale=get_locale())
        return f"Formatted Amount: {formatted_amount}"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
