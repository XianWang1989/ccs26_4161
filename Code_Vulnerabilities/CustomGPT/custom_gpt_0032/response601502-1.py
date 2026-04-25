
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data
            if request.method == 'POST':
                session['original_url'] = request.path
                session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming user authentication
        session['user_id'] = 'some_user_id'  # Set user ID
        return redirect(session.pop('original_url', '/'))
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the post request logic
    data = request.form
    return jsonify({"message": "Success", "data": data})

@app.route('/retry_protected', methods=['POST'])
def retry_protected():
    # Replay the original POST request after login
    data = session.pop('post_data', {})
    # Handle the data as needed
    return jsonify({"message": "Replayed request", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
