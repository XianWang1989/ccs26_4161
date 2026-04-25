
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your supported locales
SUPPORTED_LOCALES = ['en_US', 'fr_FR']

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(SUPPORTED_LOCALES)

class NumberForm(FlaskForm):
    amount = DecimalField(gettext('Amount'), places=2)
    submit = SubmitField(gettext('Submit'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Example of formatting the number based on locale
        user_locale = get_locale()
        locale.setlocale(locale.LC_ALL, user_locale)
        formatted_num = locale.currency(form.amount.data)
        return f"Submitted Amount: {formatted_num}"

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
