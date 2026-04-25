
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_decimal, get_locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])  # Adjust according to your supported locales

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Retrieve the raw decimal value
        raw_amount = form.amount.data
        # Format the amount according to the current locale
        formatted_amount = format_decimal(raw_amount, locale=get_locale())
        return f'Formatted Amount: {formatted_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
