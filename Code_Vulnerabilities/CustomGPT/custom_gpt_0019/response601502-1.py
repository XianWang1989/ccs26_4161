
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock function to check user authentication
def is_authenticated():
    return session.get('user_authenticated', False)

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Store original request data
            session['original_endpoint'] = request.path
            session['original_post_data'] = request.form
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        session['user_authenticated'] = True  # Assume login is successful
        original_endpoint = session.pop('original_endpoint', None)
        original_post_data = session.pop('original_post_data', None)

        if original_endpoint and original_post_data:
            # Re-execute the original POST request
            return redirect(original_endpoint, code=303)  # Use 303 for POST-redirect-GET

    return 'Login Form'  # Replace with your actual login form

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Process the original POST request
    data = request.form
    return 'Protected resource accessed with data: {}'.format(data)

if __name__ == '__main__':
    app.run()
