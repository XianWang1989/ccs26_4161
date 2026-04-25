
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, format_currency
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Set up locale
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format the number based on user's locale
        formatted_amount = format_currency(form.amount.data, 'USD', locale=get_locale())
        return f'Formatted amount: {formatted_amount}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
