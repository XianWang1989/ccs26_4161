
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_currency, get_locale

app = Flask(__name__)
app.secret_key = 'supersecretkey'
babel = Babel(app)

# Setup for localization (you'll want to expand this for other locales)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

@babel.localeselector
def get_locale_selector():
    # You can specify logic to get the user's locale here
    return get_locale().language

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()], places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()

    if form.validate_on_submit():
        # Handle the submitted form
        amount = form.amount.data
        formatted_amount = format_currency(amount, 'USD')
        flash(f'You entered: {formatted_amount}', 'success')

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
