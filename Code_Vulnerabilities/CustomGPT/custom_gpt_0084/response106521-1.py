
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Set up Babel
babel = Babel(app)

# Function to get the user's locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR', 'de_DE'])

# Define your form
class NumberForm(FlaskForm):
    amount = DecimalField('Amount', format='%.2f', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        return f'You entered: {format_decimal(amount, locale=get_locale())}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
