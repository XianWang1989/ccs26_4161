
from flask import Flask, render_template, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    # Add more languages as needed
}

@app.route('/locale/<lang>')
def set_locale(lang):
    # Set the locale based on user choice
    return redirect(request.referrer)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_number = format_decimal(form.number.data)
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
