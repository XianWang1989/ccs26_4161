
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up your locale
locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')  # Change to your desired locale

class NumberForm(FlaskForm):
    number = DecimalField('Number', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Handle the submitted number
        formatted_number = locale.format_string("%.2f", form.number.data, grouping=True)
        return f'Formatted Number: {formatted_number}'
    return render_template('index.html', form=form)

@babel.localeselector
def get_locale():
    # You can customize this to select a locale based on user preferences or request
    return 'en_US'

if __name__ == '__main__':
    app.run(debug=True)
