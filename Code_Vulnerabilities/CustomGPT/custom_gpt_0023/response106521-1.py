
from flask import Flask, render_template, request
from flask_babel import Babel, format_number
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure your supported locales
@app.before_request
def before_request():
    # Set the locale based on user preference or other logic
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Change to your needed locale

class NumberForm(FlaskForm):
    number = DecimalField('Number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        # Format the number for display
        formatted_number = format_number(number)
        return f"You entered: {formatted_number}"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
