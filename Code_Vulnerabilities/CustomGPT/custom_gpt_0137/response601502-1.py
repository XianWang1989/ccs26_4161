
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data for demonstration
users = {"user": "password"}

# Function to check if user is authenticated
def is_authenticated():
    return 'username' in session

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Save the original request data into the session
            session['original_request'] = {
                'url': request.path,
                'method': request.method,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username
            flash('Login successful!')
            # After login, check if we have a saved request
            original_request = session.pop('original_request', None)
            if original_request:
                if original_request['method'] == 'POST':
                    # Re-execute the original POST request
                    return original_post_handler(original_request['data'])
                else:
                    return redirect(original_request['url'])
            return redirect(url_for('home'))  # Redirect to home if no original request
    return 'Login Page'

@app.route('/some_protected_post', methods=['POST'])
@login_required
def some_protected_post():
    # This function should never be directly hit without login
    return 'This is a protected POST request.'

def original_post_handler(data):
    # Handle the original post logic here with the provided data
    # Example processing of form data
    return f'Handled original POST request with data: {data}'

@app.route('/')
def home():
    return 'Welcome to the home page! Please log in to access protected endpoints.'

if __name__ == '__main__':
    app.run(debug=True)
