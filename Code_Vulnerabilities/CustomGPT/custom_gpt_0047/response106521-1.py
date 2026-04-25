
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    number = DecimalField('Number', places=2, validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()

    if form.validate_on_submit():
        # Format the number based on the locale
        locale_name = get_locale()
        locale.setlocale(locale.LC_ALL, locale_name)
        formatted_number = locale.format_string("%.2f", form.number.data, grouping=True)
        return f'Formatted number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
