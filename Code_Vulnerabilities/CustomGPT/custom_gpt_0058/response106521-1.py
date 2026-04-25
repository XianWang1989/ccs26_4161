
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # This could be more complex; just using 'en' for simplicity
    return 'en'

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number:')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on locale when retrieving it
        formatted_number = format_decimal(form.number.data)
        return f'Formatted number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
