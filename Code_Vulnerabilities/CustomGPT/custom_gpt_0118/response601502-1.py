
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Simulated user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request method and data
            session['original_request_method'] = request.method
            session['original_request_path'] = request.path
            session['original_request_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['user_id'] = 'authenticated_user'  # Simulated login

        # Check if there was an original request
        if 'original_request_method' in session and session['original_request_method'] == 'POST':
            return redirect(session['original_request_path'])  # Redirecting to the original path

    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the protected POST request
    return 'Protected Resource Accessed!'

if __name__ == '__main__':
    app.run(debug=True)
