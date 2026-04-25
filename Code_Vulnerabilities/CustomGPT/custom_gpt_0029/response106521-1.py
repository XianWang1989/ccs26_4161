
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define a simple form
class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:')
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    # Here, you can implement logic to get the user's preferred language
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number according to the current locale
        formatted_number = format_decimal(form.number.data)
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
