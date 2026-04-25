
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock authentication check
def is_authenticated():
    return session.get('logged_in', False)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Store original request data in session
            session['post_data'] = request.form.to_dict() if request.method == 'POST' else None
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform authentication check
        session['logged_in'] = True  # Replace with actual authentication logic
        flash('Logged in successfully.')

        # Re-execute original POST request if there is stored data
        post_data = session.pop('post_data', None)
        if post_data:
            return redirect(url_for('protected_post', **post_data))  # Redirect with POST data

    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected_post():
    # Handle the secure POST request
    data = request.form
    return f'Protected data received: {data}'

if __name__ == '__main__':
    app.run(debug=True)
