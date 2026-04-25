
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

babel = Babel(app)

@babel.localeselector
def get_locale():
    # Set locale based on user preference, here we're using 'en_US' as default
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    number = DecimalField('Number', format='%.2f', render_kw={"step": "0.01"})
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_number = format_decimal(form.number.data)
        return f'The formatted number is: {formatted_number}'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
