
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_babel import Babel, format_decimal
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Here you'll get the raw decimal value
        amount = form.amount.data
        return f'Raw amount: {amount}, Formatted: {format_decimal(amount)}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
