
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_value = None
    if form.validate_on_submit():
        formatted_value = format_currency(form.amount.data, 'USD', locale=get_locale())

    return render_template('index.html', form=form, formatted_value=formatted_value)

if __name__ == '__main__':
    app.run(debug=True)
