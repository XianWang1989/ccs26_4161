
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

class MyForm(FlaskForm):
    amount = DecimalField('Amount', format='.2f')  # Use appropriate format
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])  # Add supported locales

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        formatted_amount = format_decimal(form.amount.data, locale=get_locale())
        return f'Formatted amount: {formatted_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
