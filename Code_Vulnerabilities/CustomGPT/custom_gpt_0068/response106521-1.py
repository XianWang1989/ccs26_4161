
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale (could be retrieved from user preferences)
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR', 'es_ES'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = None

    if form.validate_on_submit():
        amount = form.amount.data
        locale_str = get_locale()
        # Use Babel to format the number based on the user locale
        formatted_number = format_number(amount, locale=locale_str)

    return render_template('index.html', form=form, formatted_number=formatted_number)


if __name__ == "__main__":
    app.run(debug=True)
