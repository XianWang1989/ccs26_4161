
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_babel import Babel, _  
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set your available locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français'
}

@babel.localeselector
def get_locale():
    # You can set the locale based on user preference or request
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Get the submitted amount
        amount = form.amount.data
        # Format the number based on the current locale
        locale.setlocale(locale.LC_ALL, get_locale())
        formatted_amount = locale.format_string("%.2f", amount, grouping=True)
        return f'Submitted Amount: {formatted_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
