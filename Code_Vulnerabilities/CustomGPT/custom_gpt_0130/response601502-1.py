
from flask import Flask, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    # Simulated login required decorator
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate login
        session['logged_in'] = True
        original_url = session.pop('original_url', None)
        data = session.pop('post_data', None)

        if original_url and data:
            # Re-POST the data
            response = requests.post(original_url, data=data)
            return response.text  # or handle accordingly

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    return 'Protected resource accessed!'

@app.route('/handle_post', methods=['POST'])
def handle_post():
    if not session.get('logged_in'):
        # Save the original URL and POST data
        session['original_url'] = request.path
        session['post_data'] = request.form
        return redirect(url_for('login'))

    return protected()

@app.route('/home')
def home():
    return 'Welcome Home!'

if __name__ == '__main__':
    app.run(debug=True)
