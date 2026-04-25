
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock authentication check
def is_authenticated():
    return 'user_id' in session

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            session['post_data'] = request.form.to_dict()  # Store POST data in session
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        session['user_id'] = 'some_user_id'  # Simulate login
        flash('Login successful!')
        post_data = session.pop('post_data', None)  # Retrieve and remove post_data from session

        if post_data:
            # Execute the original POST request logic
            return handle_post_request(post_data)
        return redirect(url_for('home'))  # Redirect to home after login
    return 'Login Form'

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post_request():
    # Handle the actual POST request logic
    return 'POST request handled!'

@app.route('/')
def home():
    return 'Home Page'

if __name__ == "__main__":
    app.run(debug=True)
