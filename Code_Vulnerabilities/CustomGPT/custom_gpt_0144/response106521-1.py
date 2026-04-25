from flask import Flask, render_template_string, request
from flask_babel import Babel, get_locale
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import Field
from wtforms.widgets import TextInput
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['BABEL_DEFAULT_LOCALE'] = 'fr_FR'

babel = Babel(app)

class LocalizedDecimalField(Field):
    widget = TextInput()

    def _value(self):
        return str(self.data) if self.data is not None else ''

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                # Use locale to parse decimal with comma
                locale.setlocale(locale.LC_NUMERIC, str(get_locale()))
                self.data = locale.atof(valuelist[0])
            except ValueError:
                self.data = None
                raise ValueError('Invalid number format')

class MyForm(FlaskForm):
    amount = LocalizedDecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return f'Parsed number: {form.amount.data}'
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            {{ form.amount.label }}: {{ form.amount(size=20) }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
