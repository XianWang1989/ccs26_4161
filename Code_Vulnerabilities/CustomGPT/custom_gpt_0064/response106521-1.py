
from flask import Flask, render_template, request, flash
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale (can also be based on user preference)
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Change as needed

class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[InputRequired()])
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    return 'en_US'  # or get from user preferences

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on locale
        formatted_number = format_decimal(form.number.data)
        flash(f'Submitted Number: {formatted_number}', 'success')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
