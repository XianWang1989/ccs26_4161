
from flask import Flask, render_template
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Example: Define supported locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Number processing could happen here
        number = form.amount.data
        # Format number for display
        formatted_number = format_decimal(number, locale=get_locale())
        return f"Formatted Number: {formatted_number}"
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
