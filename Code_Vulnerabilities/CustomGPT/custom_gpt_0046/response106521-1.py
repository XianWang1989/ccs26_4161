
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

# Configure locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        # Format the number based on user's locale
        formatted_amount = format_currency(amount, 'USD', locale=get_locale())
        return f'Submitted amount: {formatted_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
