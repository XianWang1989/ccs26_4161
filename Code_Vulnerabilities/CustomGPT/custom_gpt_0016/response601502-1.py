
from flask import Flask, request, redirect, session, url_for, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # This should be a secure random key

# Mock user authentication
def is_user_authenticated():
    return 'user' in session

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_user_authenticated():
            # Store the original request data in session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Mock login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']  # Simple user authentication
        return redirect(url_for('post_route'))  # Redirect after login
    return 'Login Form'

@app.route('/post', methods=['POST'])
@login_required
def post_route():
    # Your normal post handling logic
    data = request.form  # Handle data directly
    return jsonify(data)

@app.route('/after_login')
def after_login():
    if 'post_data' in session:
        # Handle the stored post data after login
        post_data = session.pop('post_data')  # Retrieve and remove from session
        # Process the original request with post_data
        return jsonify(post_data)
    return 'No previous POST data.'

if __name__ == '__main__':
    app.run(debug=True)
