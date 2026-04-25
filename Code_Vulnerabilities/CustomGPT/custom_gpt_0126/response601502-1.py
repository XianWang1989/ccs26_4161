
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id'):
            # Store the original request data
            session['original_request'] = {
                'path': request.path,
                'method': request.method,
                'data': request.form.to_dict() if request.method == 'POST' else {}
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        session['user_id'] = 'some_user_id'  # Set user_id after successful login
        flash('Login successful!')

        # Check if there's a stored request
        original_request = session.pop('original_request', None)
        if original_request:
            return redirect(original_request['path'])
        return redirect(url_for('home'))
    return '<form method="post">Login form</form>'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Process the POST request data
    data = request.form
    return f"Protected data processed: {data}"

@app.route('/home')
def home():
    return "Welcome to the home page."

if __name__ == '__main__':
    app.run(debug=True)
