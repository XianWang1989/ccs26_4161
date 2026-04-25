
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_currency

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NumberForm()

    if form.validate_on_submit():
        # Process the submitted data
        number = form.number.data
        # You can format or save the number as needed
        return f'Formatted number: {format_currency(number, 'USD', locale=get_locale())}'

    return render_template('form.html', form=form)

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', format='%.2f', places=2)
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    # You can use request.accept_languages to determine the best match
    return request.accept_languages.best_match(['en_US', 'fr_FR', 'de_DE'])

if __name__ == '__main__':
    app.run(debug=True)
