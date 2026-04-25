
from flask import Flask, render_template, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define locales
locales = ['en', 'fr', 'de']  # English, French, German

@app.route('/form', methods=['GET', 'POST'])
def form_view():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        return f'Submitted number: {format_decimal(number)}'
    return render_template('form.html', form=form)

class NumberForm(FlaskForm):
    number = DecimalField('Number', format='%0.2f', places=2)
    submit = SubmitField('Submit')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(locales)

if __name__ == '__main__':
    app.run(debug=True)
