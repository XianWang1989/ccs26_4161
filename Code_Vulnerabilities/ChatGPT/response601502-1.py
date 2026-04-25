
from flask import Flask, request, redirect, url_for, session, render_template, flash, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            # Store original request data in session
            session['original_request'] = {
                'method': request.method,
                'url': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate user login...
        # If successful:
        session['user'] = 'username'  # Set the user in the session
        flash('Login successful!')

        # Check if there's an original request to handle
        original_request = session.pop('original_request', None)
        if original_request:
            method = original_request['method']
            url = original_request['url']
            data = original_request['data']

            if method == 'POST':
                return handle_post_request(data)

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Assume this function returns a response when accessed correctly
    return jsonify(message="This is a protected POST request"), 200

def handle_post_request(data):
    # This is where you handle the actual post request
    # You can call your protected route's logic directly if needed
    return jsonify(message="Successfully handled post request after login!", data=data), 200

@app.route('/')
def home():
    return "Welcome to the home page! <a href='/protected'>Protected POST</a>"

if __name__ == '__main__':
    app.run(debug=True)
