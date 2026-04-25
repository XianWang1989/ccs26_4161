
from flask import Flask, render_template, request, flash
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired
import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
babel = Babel(app)

# Set the locale for the app (this can be improved by user preferences)
@babel.localeselector
def get_locale():
    return 'fr'  # Change this according to your locale

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        amount = form.amount.data
        flash(f'Formatted amount: {format_decimal(amount)}')
        return render_template('index.html', form=form)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
