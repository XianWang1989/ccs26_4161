
from flask import Flask, render_template, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up a locale
@babel.localeselector
def get_locale():
    # You can also change this logic according to your needs
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Get the number and process it
        number = form.number.data
        # Do something with the number (e.g., store it, process it, etc.)
        return f'You entered: {format_decimal(number)}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
