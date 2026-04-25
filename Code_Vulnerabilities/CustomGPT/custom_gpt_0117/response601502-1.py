
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store request data in session
            session['original_url'] = request.url
            session['original_params'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user (this is just a placeholder)
        session['logged_in'] = True
        flash('Logged in successfully.')

        # Re-execute the original POST request if exists
        if 'original_url' in session and 'original_params' in session:
            original_url = session.pop('original_url')
            original_params = session.pop('original_params')
            return redirect(original_url)  # Or use a custom function to handle the params

    return "Login Page"

@app.route('/secure-endpoint', methods=['POST'])
@login_required
def secure_endpoint():
    # Logic for when user is logged in and POST request is valid
    data = request.form
    return f"Received data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
