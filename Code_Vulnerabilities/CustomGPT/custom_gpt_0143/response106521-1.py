
from flask import Flask, render_template
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
babel = Babel(app)

# Configure your locales
@babel.localeselector
def get_locale():
    return 'fr'  # Set your default or user-specific locale

class NumberForm(FlaskForm):
    number = DecimalField('Number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = None
    if form.validate_on_submit():
        formatted_number = format_decimal(form.number.data)

    return render_template('index.html', form=form, formatted_number=formatted_number)

if __name__ == '__main__':
    app.run()
