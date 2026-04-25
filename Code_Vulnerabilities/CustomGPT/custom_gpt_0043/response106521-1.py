
from flask import Flask, render_template, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

# Define supported locales
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

# Example form with a decimal field
class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    # You can also use request.accept_languages to get the best match if desired
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on the current locale
        formatted_number = format_decimal(form.number.data)
        return f'Formatted Number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
