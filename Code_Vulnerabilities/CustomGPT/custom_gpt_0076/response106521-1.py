
from flask import Flask, render_template, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, _

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Example locales
locales = {
    'en': 'en_US',
    'fr': 'fr_FR',
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(locales.keys())

class NumberForm(FlaskForm):
    amount = DecimalField(_('Amount'), places=2)
    submit = SubmitField(_('Submit'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        flash(_('Submitted amount: %s') % format_number(form.amount.data), 'success')
        return redirect('/')
    return render_template('index.html', form=form)

def format_number(value):
    locale = get_locale()
    from babel.numbers import format_decimal
    return format_decimal(value, locale=locales[locale])

if __name__ == '__main__':
    app.run(debug=True)
