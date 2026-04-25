
from flask import Flask, request, session, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Mock function to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:  # If user isn't logged in
            # Store original request data
            session['original_request'] = {
                'method': request.method,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))  # Redirect to login
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate logging the user in
        session['logged_in'] = True
        # After logging in, handle the original request if available
        original_request = session.pop('original_request', None)
        if original_request and original_request['method'] == 'POST':
            # Re-execute the POST request
            return handle_post(original_request['data'])
    return 'Login Page'

@app.route('/protected-endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    # Handle the POST request here
    return 'Original POST request executed!'

def handle_post(data):
    # Function to handle the POST data after login
    return f'Post executed with data: {data}'

if __name__ == '__main__':
    app.run(debug=True)
