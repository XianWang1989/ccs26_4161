
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Sample locale settings
@babel.localeselector
def get_locale():
    return 'fr'  # Change this to dynamically select based on user preference

class NumberForm(FlaskForm):
    number = DecimalField('Number', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = ''

    if form.validate_on_submit():
        # Get the number from form and format it based on locale
        formatted_number = format_decimal(form.number.data)

    return render_template('index.html', form=form, formatted_number=formatted_number)

if __name__ == '__main__':
    app.run(debug=True)
