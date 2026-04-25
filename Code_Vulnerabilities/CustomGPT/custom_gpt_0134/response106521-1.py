
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal, get_locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define a simple form
class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@babel.localeselector
def get_lang():
    return get_locale()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number according to the current locale
        formatted_amount = format_decimal(form.amount.data, locale=get_lang())
        return f"Submitted Amount: {formatted_amount}"

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
