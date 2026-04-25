
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField
from flask_babel import Babel, _

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configuring locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class LocalizedDecimalField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                # Parse the incoming string to a decimal
                # Customize based on the locale
                self.data = self.string_to_number(valuelist[0])
            except ValueError:
                self.data = None
                raise ValueError(_('Invalid input'))

    def string_to_number(self, value):
        # This is where you handle locale logic
        if request.accept_languages.best_match(['fr']):
            # French locale (e.g., 1.234,56)
            value = value.replace('.', '').replace(',', '.')
        elif request.accept_languages.best_match(['de']):
            # German locale (e.g., 1.234,56)
            value = value.replace('.', '').replace(',', '.')
        return float(value)

class ExampleForm(FlaskForm):
    amount = LocalizedDecimalField('Amount')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExampleForm()
    if form.validate_on_submit():
        return f'Amount: {form.amount.data}'

    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
