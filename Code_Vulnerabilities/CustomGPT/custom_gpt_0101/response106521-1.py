
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    number = DecimalField('Number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Access the number in the submitted locale format
        number = form.number.data
        formatted_number = format_number(number)
        return f'Formatted Number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
