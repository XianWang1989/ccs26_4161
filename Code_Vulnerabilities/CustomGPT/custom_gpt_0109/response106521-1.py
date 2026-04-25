
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.secret_key = 'secret!'
babel = Babel(app)

# Configure your supported locales
languages = ['en', 'fr']  # English and French
babel.init_app(app, default_locale='en', supported_locales=languages)

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Here, you get the raw value from the form
        raw_amount = form.amount.data
        # Format it based on the current locale
        formatted_amount = format_decimal(raw_amount)
        return f'The formatted amount is: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
