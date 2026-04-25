
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define supported locales
class Config:
    LANGUAGES = ['en', 'fr', 'es']

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Form definition
class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:', number_format='%.2f')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        # Format with the current locale
        formatted_number = format_number(number)
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
