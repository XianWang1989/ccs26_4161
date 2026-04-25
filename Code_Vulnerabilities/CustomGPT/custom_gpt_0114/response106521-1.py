
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

babel = Babel(app)

@babel.localeselector
def get_locale():
    # Here you can return the user's preferred locale, e.g., from session or request
    return 'en_US'  # Change as necessary

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', validators=[DataRequired()], places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number using the current locale
        formatted_number = format_number(form.number.data)
        return f'Formatted number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
