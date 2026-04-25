
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Dummy locale getter
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Process the input (you'll get it in decimal format)
        input_value = form.amount.data
        # Here you can use format_decimal for displaying the value
        formatted_value = format_decimal(input_value)
        return f"Formatted Amount: {formatted_value}"

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
