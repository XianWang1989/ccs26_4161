
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'fr'])  # Add your desired locales here

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2, default=0.00)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the input using the current locale
        formatted_amount = format_decimal(form.amount.data)
        return f'Submitted amount: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
