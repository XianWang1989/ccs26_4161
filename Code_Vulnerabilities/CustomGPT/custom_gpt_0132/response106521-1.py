
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_babel import Babel, ngettext
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define supported languages
@babel.localeselector
def get_locale():
    return 'fr'  # or use request.accept_languages.best_match(['en', 'fr'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', places=2, validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Here, you could process the submitted number
        amount = form.amount.data
        formatted_amount = format_currency(amount)
        return f'Submitted Amount: {formatted_amount}'
    return render_template('index.html', form=form)

def format_currency(amount):
    return f"{amount:,.2f}"  # Format the number (you might want to customize this to use babel)

if __name__ == '__main__':
    app.run(debug=True)
