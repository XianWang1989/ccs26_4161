
from flask import Flask, render_template, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # You can define logic to get the user's locale here
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on the locale
        formatted_amount = format_decimal(form.amount.data)
        return f'Formatted Amount: {formatted_amount}'
    return render_template('form.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
