
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from flask_babel import Babel, format_number
import locale

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

# Configure Babel
@babel.localeselector
def get_locale():
    return 'en_US'  # You can use a dynamic approach to get the user's locale

class NumberForm(FlaskForm):
    number = FloatField('Enter a number:')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Handle the submitted number
        formatted_number = format_number(form.number.data)
        # Do something with the formatted number
        return f'You entered: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
