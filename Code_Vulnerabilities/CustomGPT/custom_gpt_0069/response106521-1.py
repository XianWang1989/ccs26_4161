
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_number

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your supported locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.amount.data
        # Format the number according to the selected locale
        formatted_number = format_number(number)
        return f"Formatted number: {formatted_number}"
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
