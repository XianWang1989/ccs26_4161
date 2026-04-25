
from flask import Flask, session, redirect, url_for, request, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user authentication for demonstration
def is_authenticated():
    return 'username' in session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Store the original request data
            session['next_post'] = request.get_json()  # Capture POST data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume successful login, save username in session
        session['username'] = request.form['username']
        flash('Login successful!')
        # After login, check if we have a stored POST request
        if 'next_post' in session:
            post_data = session.pop('next_post')  # Retrieve and remove from session
            return handle_post_request(post_data)  # Handle the stored POST request
        return redirect(url_for('home'))
    return 'Login form here'  # Show login form

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the protected POST request
    return 'This is a protected POST response!'

def handle_post_request(post_data):
    # Handle the POST request with provided data
    return 'Handled POST request with data: {}'.format(post_data)

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
