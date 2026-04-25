
from flask import Flask, render_template, request, flash
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on the current locale
        formatted_number = format_number(form.number.data)
        flash(f'Formatted Number: {formatted_number}', 'success')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
