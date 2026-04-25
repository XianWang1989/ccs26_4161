
from flask import Flask, render_template
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configuring locales
@app.before_request
def before_request():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set to your preferred locale

class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    return 'en_US'  # Adjust this to get the user locale if needed

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Process the number here
        formatted_number = format_decimal(form.number.data, locale='en_US')
        return f'The formatted number is: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
