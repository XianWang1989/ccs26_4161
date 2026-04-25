
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale according to user preferences or request
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    number = DecimalField('Localized Number', format='%.2f')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on the user's locale
        formatted_number = format_decimal(form.number.data)
        return f'Formatted Number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
