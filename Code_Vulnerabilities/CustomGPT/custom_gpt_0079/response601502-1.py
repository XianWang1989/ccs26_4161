
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock function for checking login
def is_logged_in():
    return 'user_id' in session

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store URL and request data
            session['post_data'] = request.form.to_dict()
            session['next_url'] = request.url
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        session['user_id'] = 'example_user_id'  # Set user id after login
        next_url = session.get('next_url')
        # Execute stored POST request after logging in
        if next_url and 'post_data' in session:
            post_data = session.pop('post_data')
            session.pop('next_url')
            return redirect(next_url)  # We redirect instead of executing POST
        return redirect(url_for('home'))  # Default redirect after login
    return 'Login Page'

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    # Handle your POST submission
    return 'Form submitted!'

@app.route('/home')
def home():
    return 'Welcome to the homepage!'

if __name__ == '__main__':
    app.run(debug=True)
