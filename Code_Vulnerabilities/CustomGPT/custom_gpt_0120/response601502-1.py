
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the original request data
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['logged_in'] = True
        flash('Logged in successfully!')
        return redirect(url_for('handle_post'))

    return 'Login Page'

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post():
    # Process the POST request here
    return 'POST request handled'

@app.route('/original_endpoint', methods=['POST'])
@login_required
def original_endpoint():
    # Handle the initial request logic
    return 'Original POST request handled'

@app.route('/login_redirect', methods=['POST'])
def login_redirect():
    # Check for original data in the session
    original_data = session.pop('original_data', None)
    if original_data:
        # Re-execute the original POST request
        return original_endpoint(**original_data)
    return 'No data to process'

if __name__ == '__main__':
    app.run(debug=True)
