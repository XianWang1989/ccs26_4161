
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalField
from flask_babel import Babel, format_decimal
from babel import Locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Example supported locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch',
}

@app.route('/form', methods=['GET', 'POST'])
def form_view():
    form = MyForm()

    if form.validate_on_submit():
        # Use the formatted number for further processing
        number = form.number.data
        return f"Received: {number}"

    return render_template('form.html', form=form)

class MyForm(FlaskForm):
    number = DecimalField('Number', places=2)

@babel.localeselector
def get_locale():
    # You can customize this function to return user's preferred locale
    return request.accept_languages.best_match(LANGUAGES.keys())

if __name__ == '__main__':
    app.run(debug=True)
