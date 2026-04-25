
from flask import Flask, request, redirect, session, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Example login_required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the request data
            session['post_data'] = request.form.to_dict()
            session['post_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic, authenticate user
        session['logged_in'] = True  # Set the user's login status
        return redirect(session.pop('post_url', url_for('index')))
    return 'Login Form'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    data = request.form
    return f"Processed data: {data}"

@app.route('/')
def index():
    return 'Welcome to the app!'

if __name__ == '__main__':
    app.run(debug=True)
