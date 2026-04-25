
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure Babel for locale selection
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

# Custom DecimalField with locale formatting
class LocalizedDecimalField(DecimalField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                value = valuelist[0].replace(',', '')  # Change this as needed for locale
                self.data = self.coerce(value)
            except ValueError:
                self.data = None
                raise ValueError(gettext('Invalid input.'))

class MyForm(FlaskForm):
    amount = LocalizedDecimalField('Amount', places=2)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process the form data
        return 'Valid amount: {}'.format(form.amount.data)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
