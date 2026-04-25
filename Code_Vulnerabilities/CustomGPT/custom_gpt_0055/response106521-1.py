
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        # You can format the number here based on the locale if needed
        return f'You entered: {number}'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
