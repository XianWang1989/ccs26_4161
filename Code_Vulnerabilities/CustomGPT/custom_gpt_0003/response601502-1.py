
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            # Store the original request data
            session['original_request'] = {
                'endpoint': request.path,
                'data': request.form.to_dict(),
                'method': request.method
            }
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user authentication happens here
        session['user'] = request.form['username']  # Simplified login process
        # Check for original request in session
        original_request = session.pop('original_request', None)
        if original_request:
            # Re-execute the original request
            if original_request['method'] == 'POST':
                return handle_post_request(original_request['data'])
        return redirect(url_for('home'))  # Redirect to home after login
    return 'Login Form'  # Render your login form here

@app.route('/post-endpoint', methods=['POST'])
@login_required
def handle_post_request():
    data = request.form
    # Handle your POST data here
    return jsonify({"message": "POST request handled!", "data": data})

@app.route('/')
def home():
    return 'Welcome to the homepage! Please <a href="/login">login</a>.'

if __name__ == '__main__':
    app.run(debug=True)
