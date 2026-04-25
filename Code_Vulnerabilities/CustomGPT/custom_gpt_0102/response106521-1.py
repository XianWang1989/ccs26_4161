
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
babel = Babel(app)

# Define your locale, e.g., 'en_US', 'fr_FR', etc.
@babel.localeselector
def get_locale():
    return 'fr_FR'  # Change this based on user preferences

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_number = format_decimal(form.number.data, locale=get_locale())
        flash(f'Formatted number: {formatted_number}')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
