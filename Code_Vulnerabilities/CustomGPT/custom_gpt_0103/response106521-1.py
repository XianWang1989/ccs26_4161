
from flask import Flask, render_template_string, request
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from flask_babel import Babel, format_number

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Dummy locale; you can change it as needed
@babel.localeselector
def get_locale():
    return 'fr'  # Example: French locale

class NumberForm(FlaskForm):
    number = DecimalField('Number', places=2)
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    formatted_number = None

    if form.validate_on_submit():
        value = form.number.data
        formatted_number = format_number(value)  # Format the number based on locale

    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            {{ form.number.label }} {{ form.number(size=10) }} <br>
            {{ form.submit() }}
        </form>
        {% if formatted_number %}
            <p>Formatted Number: {{ formatted_number }}</p>
        {% endif %}
    ''', form=form, formatted_number=formatted_number)

if __name__ == '__main__':
    app.run(debug=True)
