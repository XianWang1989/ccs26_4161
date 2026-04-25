
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock authentication check
def is_logged_in():
    return session.get('logged_in', False)

# Custom decorator for login requirement
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store the original request details
            session['request_method'] = request.method
            session['request_path'] = request.path
            session['request_form'] = request.form.to_dict() if request.method == "POST" else {}
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume authentication happens here
        session['logged_in'] = True
        # Check if there was a stored request
        if 'request_path' in session:
            return redirect(session['request_path'])
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Here, you can handle the actual POST request if authenticated
    return jsonify({"message": "This is a protected resource!"})

@app.route('/perform_post', methods=['POST'])
@login_required
def perform_post():
    # Handle the post action
    return jsonify({"data": request.form})

if __name__ == '__main__':
    app.run(debug=True)
