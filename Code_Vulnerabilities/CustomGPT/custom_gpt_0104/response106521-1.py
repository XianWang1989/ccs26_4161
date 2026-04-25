
from flask import Flask, render_template
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define available locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch'
}

@babel.localeselector
def get_locale():
    # You can use request.args or request.accept_languages to decide
    return 'fr'  # Set this based on logic (e.g. user preference)

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Here you can use the number submitted and format it
        localized_amount = format_currency(form.amount.data, 'USD')
        return f'Formatted Amount: {localized_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
