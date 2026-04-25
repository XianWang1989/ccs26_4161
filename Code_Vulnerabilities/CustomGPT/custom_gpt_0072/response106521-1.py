
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your locales here
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class LocalizedDecimalField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            value = valuelist[0]
            # Assuming the locale formatting is handled in `format_decimal`
            self.data = self.parse_locale_number(value)

    def parse_locale_number(self, value):
        # Custom logic to parse locale numbers
        # Adapt as necessary based on your locale
        try:
            return format_decimal(value)  # Replace with your parsing logic
        except ValueError:
            raise ValueError('Invalid number format.')

class MyForm(FlaskForm):
    number = LocalizedDecimalField('Number', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        number = form.number.data
        return f'Number submitted: {number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
