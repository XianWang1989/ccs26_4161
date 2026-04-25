
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy login check
def is_authenticated():
    return 'user_id' in session

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Store original request data
            session['original_post'] = request.form.to_dict()
            session['original_url'] = request.path
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume authentication succeeds
        session['user_id'] = 'some_user_id'
        if 'original_post' in session:
            # Proceed with the original POST request
            original_data = session.pop('original_post')
            original_url = session.pop('original_url')
            return redirect(original_url)  # redirect to the original URL
    return "Login Form"

@app.route('/protected-endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    # This will be executed if the user is logged in
    data = request.form
    return jsonify({"message": "Success", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
