
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from flask_babel import Babel, format_number
import locale

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en_US', 'fr_FR'])

class NumberForm(FlaskForm):
    number = FloatField('Number')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NumberForm()
    if form.validate_on_submit():
        number = form.number.data
        return render_template('result.html', number=format_number(number))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
