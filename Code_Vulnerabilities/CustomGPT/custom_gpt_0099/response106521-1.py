
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
babel = Babel(app)

# Define your locale choices
LOCALES = {'en': 'en_US', 'fr': 'fr_FR'}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LOCALES.keys())

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_amount = format_decimal(form.amount.data, locale=get_locale())
        return f'Formatted Amount: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
