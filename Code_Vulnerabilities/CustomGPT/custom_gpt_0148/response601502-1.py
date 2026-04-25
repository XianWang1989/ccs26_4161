
from flask import Flask, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock function to check if user is logged in
def is_logged_in():
    return 'user_id' in session

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store original request info in session
            session['original_url'] = request.path
            session['original_method'] = request.method
            session['original_data'] = request.form.to_dict() if request.method == 'POST' else {}
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user authentication is successful
        session['user_id'] = 'authenticated_user'
        # Check if there was an original request
        original_method = session.pop('original_method', None)
        if original_method == 'POST':
            # Recreate the POST request
            return handle_original_post(session.pop('original_url', ''), session.pop('original_data', {}))
        return redirect(url_for('home'))  # Redirect after login
    return 'Login Page'  # Render login form here

@login_required
@app.route('/protected', methods=['POST'])
def protected():
    # Handle your protected POST request here
    return 'This is a protected resource!'

def handle_original_post(url, data):
    with app.test_request_context(path=url, method='POST', data=data):
        return globals()[url[1:]]()  # Call the original function directly

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
