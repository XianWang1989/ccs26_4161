
from flask import Flask, session, redirect, url_for, request, flash
from flask import jsonify
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock user database
users = {"user": "hashed_password"}  # Replace with actual hashed password

def login_required(f):
    def decorator(*args, **kwargs):
        if 'user' not in session:
            # Store original request details if not logged in
            session['next_url'] = request.path
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorator

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user, password):
            session['user'] = username
            # Redirect to the original POST request
            return handle_post_after_login()
        flash('Invalid credentials')
    return 'Login Form Here'  # Render your login form

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle your POST request
    return jsonify({"message": "Successful POST request", "data": request.form})

def handle_post_after_login():
    """Resend the original POST request."""
    post_data = session.pop('post_data', None)
    if post_data:
        return jsonify({"message": "Re-executed POST", "data": post_data})
    return redirect(url_for('some_default_route'))

if __name__ == '__main__':
    app.run(debug=True)
