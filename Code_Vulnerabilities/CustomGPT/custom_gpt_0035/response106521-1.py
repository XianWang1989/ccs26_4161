
from flask import Flask, render_template_string, request
from flask_babel import Babel, format_decimal
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Configure local selection
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    amount = DecimalField('Amount')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        formatted_amount = format_decimal(form.amount.data)
        return f'The formatted amount is: {formatted_amount}'
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            <p>{{ form.amount.label }} {{ form.amount() }}</p>
            <p>{{ form.submit() }}</p>
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
