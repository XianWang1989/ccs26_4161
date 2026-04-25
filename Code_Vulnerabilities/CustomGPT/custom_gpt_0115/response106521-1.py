
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_number

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Set up Babel
babel = Babel(app)

# Example locales
locales = {
    'en': 'en_US',
    'fr': 'fr_FR',
    'de': 'de_DE'
}

@babel.localeselector
def get_locale():
    # Just for demonstration; in a real app, you'd get this from user preferences
    return request.args.get('lang', 'en')

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_number = format_number(form.number.data, locale=get_locale())
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
