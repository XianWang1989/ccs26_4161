
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_babel import Babel, format_decimal
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

babel = Babel(app)

# Define your custom form
class NumberForm(FlaskForm):
    number = DecimalField('Number:', places=2)
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    # Return the user's preferred language; default to 'en'
    return request.accept_languages.best_match(['en', 'fr', 'es'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()

    if form.validate_on_submit():
        # This will return a formatted number based on the selected locale
        formatted_number = format_decimal(form.number.data, locale=get_locale())
        return f'The formatted number is: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
