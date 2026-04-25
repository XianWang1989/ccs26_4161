
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the request for later
            session['original_request'] = {
                'path': request.path,
                'method': request.method,
                'data': request.form.to_dict()  # Store form data
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate the user (this is just a stub)
        session['user_id'] = 'authenticated_user'  # Simulate successful login

        # After login, check for stored request
        original_request = session.pop('original_request', None)
        if original_request:
            return redirect(url_for(original_request['path'], **original_request['data']))

        return redirect(url_for('home'))
    return "Login Page"

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    data = request.form
    # Process the POST request
    return jsonify({"message": "Success", "data": data})

@app.route('/home')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
