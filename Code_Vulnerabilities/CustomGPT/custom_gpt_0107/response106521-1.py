
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, lazy_gettext as _

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
babel = Babel(app)

# Define your supported languages
LANGUAGES = {
    'en': 'English',
    'fr': 'French',
    'de': 'German'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

class NumberForm(FlaskForm):
    number = DecimalField(_('Number'), format='%.2f')  # You can customize the format
    submit = SubmitField(_('Submit'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Process the number
        formatted_number = format(form.number.data, '.2f')
        return f"Submitted number: {formatted_number}"

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
