
from flask import Flask, render_template
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure available languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch'
}

@babel.localeselector
def get_locale():
    return 'fr'  # Change according to your needs.

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        formatted_amount = format_currency(amount, 'EUR')  # Use appropriate currency
        return f'Submitted amount: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
