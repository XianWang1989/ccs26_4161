
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', format='%.2f')  # Use appropriate format
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = format_decimal(form.number.data, locale=get_locale())
        return f'Formatted number: {number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
