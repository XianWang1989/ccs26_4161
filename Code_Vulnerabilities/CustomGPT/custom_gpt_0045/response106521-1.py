
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define the form
class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', places=2)
    submit = SubmitField('Submit')

# Define supported locales
SUPPORTED_LOCALES = ['en', 'fr', 'de']

@babel.localeselector
def get_locale():
    # Allow the client to choose the locale via URL argument
    return request.args.get('lang', 'en')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = ''

    if form.validate_on_submit():
        # Retrieve and format the number based on the locale
        formatted_number = format(form.number.data, ',.2f')  # Default formatting

        if get_locale() == 'fr':
            formatted_number = "{:,.2f}".format(form.number.data).replace(',', ' ').replace('.', ',')
        elif get_locale() == 'de':
            formatted_number = "{:,.2f}".format(form.number.data).replace('.', ',')

    return render_template('index.html', form=form, formatted_number=formatted_number)

if __name__ == '__main__':
    app.run(debug=True)
