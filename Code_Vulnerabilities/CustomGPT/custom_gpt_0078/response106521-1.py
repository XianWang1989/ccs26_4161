
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from wtforms import Form, DecimalField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
babel = Babel(app)

# Configure your locales
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

# Initialize your form
class NumberForm(Form):
    amount = DecimalField('Amount', places=2, validators=[InputRequired()])
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    # You can return the user preferred language based on some criteria
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        formatted_amount = format_number(amount)  # Format the number according to the locale
        return f'Formatted Amount: {formatted_amount}'  # Output the formatted number

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
