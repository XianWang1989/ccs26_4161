
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulate a user login check
def is_logged_in():
    return session.get('user_logged_in')

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store the original request data
            session['original_request'] = {
                'url': request.path,
                'data': request.form.to_dict()  # Keep form data
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ... handle login logic ...
        session['user_logged_in'] = True
        flash('Login successful!')

        # Check if there was an original request
        original_request = session.pop('original_request', None)
        if original_request:
            return redirect(original_request['url'], code=307)

        return redirect(url_for('home'))

    return "<form method='post'>Login Form Here</form>"

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    data = request.form
    return f"Received data: {data}"

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run()
