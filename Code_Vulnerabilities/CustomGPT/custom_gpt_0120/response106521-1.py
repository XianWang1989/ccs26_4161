
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_babel import Babel, _

import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set the locale configuration
def set_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

babel.init_app(app, locale_selector=set_locale)

# Define the form
class NumberForm(FlaskForm):
    number = StringField(_('Number'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Retrieve and format the number
        raw_number = form.number.data
        try:
            # Set locale for formatting
            locale.setlocale(locale.LC_ALL, set_locale())
            formatted_number = locale.currency(float(raw_number), grouping=True)
        except (ValueError, TypeError):
            formatted_number = _('Invalid number')

        return render_template('result.html', formatted_number=formatted_number)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
