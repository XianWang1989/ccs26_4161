
from flask import Flask
from flask_babel import Babel
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # For simplicity, using a fixed locale; you can customize this
    return 'fr'  # Change to 'en', 'de', etc., based on your requirement
