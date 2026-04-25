
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, Locale

app = Flask(__name__)
app.secret_key = 'your_secret_key'
babel = Babel(app)

# Define the available locales
locales = ['en', 'fr', 'de']

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(locales)

# Custom DecimalField for localized input
class LocalizedDecimalField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                # Use locale-based formatting to parse the input
                locale = get_locale()
                number = valuelist[0].replace(',', '.').replace(' ', '')
                # Convert to the appropriate number format
                self.data = float(number)
            except ValueError:
                raise ValueError('Invalid input for a number.')

class NumberForm(FlaskForm):
    number = LocalizedDecimalField('Number:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        flash(f'Number entered: {form.number.data}', 'success')
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
