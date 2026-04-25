
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, _
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR', 'de_DE'])

class NumberForm(FlaskForm):
    amount = DecimalField(_('Amount'), places=2)
    submit = SubmitField(_('Submit'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Get the locale for formatting
        current_locale = get_locale()
        locale.setlocale(locale.LC_ALL, current_locale)

        # Format the number based on the locale
        formatted_number = locale.format_string('%.2f', form.amount.data, grouping=True)
        return f'Formatted Number: {formatted_number}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
