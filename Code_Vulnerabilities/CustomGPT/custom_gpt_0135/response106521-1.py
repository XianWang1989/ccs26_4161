
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Change this to your desired locale

babel = Babel(app)

# Define a simple form
class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number according to the locale
        formatted_number = format_number(form.number.data)
        return f'Formatted number: {formatted_number}'

    return render_template('index.html', form=form)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

if __name__ == '__main__':
    app.run(debug=True)
