
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define a custom DecimalField for locale-specific formatting
class LocalizedDecimalField(DecimalField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                # Parse the input to a Decimal
                self.data = self.coerce(valuelist[0].replace(',', ''))  # Replace for locale formatting
            except ValueError:
                self.data = None
                raise ValueError('Invalid decimal value')

    def __call__(self, **kwargs):
        # Format the output using the current locale
        return super().__call__(**kwargs) + f' (formatted: {format_number(self.data, locale=get_locale())})'

class MyForm(FlaskForm):
    amount = LocalizedDecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Handle the localized number input
        return f'You entered: {form.amount.data}'
    return render_template('index.html', form=form)

@babel.localeselector
def get_locale():
    # You can use request.accept_languages to determine the best match
    return request.accept_languages.best_match(['en', 'fr', 'de'])

if __name__ == '__main__':
    app.run(debug=True)
