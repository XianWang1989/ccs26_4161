
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale based on user preference (e.g., via a user profile or request)
@babel.localeselector
def get_locale():
    return 'fr_FR'  # Change this based on your application's needs

class NumberForm(FlaskForm):
    number = DecimalField('Localized Number', format='%.2f')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()

    if form.validate_on_submit():
        # Access the submitted number
        raw_value = form.number.data
        formatted_value = format_decimal(raw_value, locale=get_locale())  # Format number
        return f'Formatted Number: {formatted_value}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
