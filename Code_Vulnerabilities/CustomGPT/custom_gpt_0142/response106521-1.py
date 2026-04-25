
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure the locales supported
@app.before_request
def before_request():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set default locale

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR', 'de_DE'])

class MyForm(FlaskForm):
    number = FloatField('Enter a number:')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Here you can use format_number for displaying
        localized_number = format_number(form.number.data)
        return f'The formatted number is: {localized_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
