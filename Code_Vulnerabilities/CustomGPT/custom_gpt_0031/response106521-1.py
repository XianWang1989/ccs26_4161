
from flask import Flask, render_template_string, request, flash
from flask_wtf import FlaskForm
from flask_babel import Babel, format_number
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up Flask-Babel
babel = Babel(app)

# Configure locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'])

class NumberForm(FlaskForm):
    number = DecimalField('Enter a number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Here you can format the number based on the locale
        formatted_number = format_number(form.number.data)
        flash(f'Formatted number: {formatted_number}', 'success')

    return render_template_string('''
        <!doctype html>
        <title>Localized Numbers</title>
        <h1>Localized Number Form</h1>
        <form method="post">
            {{ form.number.label }} {{ form.number() }}<br>
            {% for error in form.number.errors %}
                <span style="color:red;">[{{ error }}]</span>
            {% endfor %}
            <br>
            {{ form.submit() }}
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
