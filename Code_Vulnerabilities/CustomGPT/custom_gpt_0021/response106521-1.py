
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_babel import Babel, format_currency
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Example locale configuration
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

# Form definition
class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_amount = None
    if form.validate_on_submit():
        amount = form.amount.data
        # Format the number based on the user's locale
        formatted_amount = format_currency(amount, 'USD', locale=get_locale())
    return render_template('index.html', form=form, formatted_amount=formatted_amount)

if __name__ == '__main__':
    app.run(debug=True)
