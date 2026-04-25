
from flask import Flask, render_template, request
from flask_babel import Babel, format_currency
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # You can set the locale based on user preferences or accept-Language header
    return 'fr'  # Example: setting locale to French

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_amount = format_currency(form.amount.data, 'EUR')
        return f'Formatted Amount: {formatted_amount}'

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
