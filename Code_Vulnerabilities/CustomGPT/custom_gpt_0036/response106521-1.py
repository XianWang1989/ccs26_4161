
from flask import Flask, request, render_template_string
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal
from decimal import Decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
babel = Babel(app)

# Configure locales
@app.route('/locales', methods=['GET', 'POST'])
def locales():
    form = NumberForm()
    if form.validate_on_submit():
        # Get the input correctly formatted
        number = form.number.data
        return render_template_string('''
            <p>Received Number: {{ number }}</p>
            <p>Formatted Number: {{ formatted_number }}</p>
        ''', number=number, formatted_number=format_decimal(number))
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            {{ form.number.label }} {{ form.number(size=10) }} <br>
            {{ form.submit() }}
        </form>
    ''', form=form)

# Define the form with a DecimalField
class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:', places=2)
    submit = SubmitField('Submit')

# Define the locale selector
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

if __name__ == '__main__':
    app.run(debug=True)
