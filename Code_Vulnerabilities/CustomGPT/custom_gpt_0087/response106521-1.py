
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Example locales
LOCALES = ['en', 'fr', 'de']  # English, French, German

# Function to select the locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LOCALES)

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = None
    if form.validate_on_submit():
        # Format the submitted number according to the current locale
        formatted_number = format_number(form.number.data)

    return render_template('index.html', form=form, formatted_number=formatted_number)

if __name__ == '__main__':
    app.run(debug=True)
