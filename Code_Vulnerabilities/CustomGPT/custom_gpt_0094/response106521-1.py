
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure your locales
app.config['BABEL_DEFAULT_LOCALE'] = 'en_US'

# Locale selector
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Formatting the number based on the selected locale
        formatted_amount = format_decimal(form.amount.data, locale=get_locale())
        return f"Formatted Amount: {formatted_amount}"

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
