
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from flask_babel import Babel, format_number
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

# Define your locales
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'es'])

class NumberForm(FlaskForm):
    number = DecimalField('Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        # Format number based on the locale
        formatted_number = format_number(form.number.data)
        flash(f'Formatted number: {formatted_number}')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
