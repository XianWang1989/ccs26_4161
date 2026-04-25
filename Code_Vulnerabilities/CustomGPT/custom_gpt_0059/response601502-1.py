
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user authentication status
is_authenticated = False

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    global is_authenticated
    # Handle login logic (e.g., verify user credentials)
    if request.method == 'POST':
        # Assume user logged in successfully
        is_authenticated = True
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the protected post request
    return 'Protected POST request processed'

@app.route('/request_protected', methods=['POST'])
def request_protected():
    if not is_authenticated:
        session['next_url'] = request.url
        session['form_data'] = request.form
        return redirect(url_for('login'))

    # Process the request immediately if authenticated
    return protected()

@app.route('/login_protected', methods=['POST'])
def login_protected():
    # After login, handle the original post request
    form_data = session.pop('form_data', None)
    if form_data:
        # Process original form data
        return 'Protected POST request processed with original data: ' + str(form_data)
    return 'No data found'

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
