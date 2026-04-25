
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Setup Babel
babel = Babel(app)

# Set the locale for the user (can be done dynamically)
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de', 'es'])

class NumberForm(FlaskForm):
    amount = DecimalField('Enter Amount', format='%.2f')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_amount = None
    if form.validate_on_submit():
        # Get the amount as a float
        amount = form.amount.data
        # Format the number based on the current locale
        formatted_amount = format_number(amount)

    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
