
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Configure the supported locales
LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch',
}

@babel.localeselector
def get_locale():
    # Detect the user's preferred language
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.route('/', methods=['GET', 'POST'])
def index():
    number = None
    if request.method == 'POST':
        number = request.form.get('number')
        # Process the number based on locale (e.g., convert to float)

    return render_template('index.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
