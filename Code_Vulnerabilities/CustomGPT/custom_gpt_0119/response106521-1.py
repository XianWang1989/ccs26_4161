
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_number

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

babel = Babel(app)

# Define a simple form with a DecimalField
class NumberForm(FlaskForm):
    number = DecimalField('Enter a number: ', places=2)
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Get the locale-specific formatted number
        formatted_number = format_number(form.number.data)
        return f'Submitted number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
