
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up the available locales
locales = ['en_US', 'fr_FR']

@babel.localeselector
def get_locale():
    # You can return local based on user preference; here we use a default for demonstration
    return request.accept_languages.best_match(locales)

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number according to the locale
        localized_amount = format_decimal(form.amount.data)
        return f'Formatted Amount: {localized_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
