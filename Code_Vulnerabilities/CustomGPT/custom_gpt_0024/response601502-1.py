
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mocked authentication state
authenticated = False

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not authenticated:
            session['original_post'] = request.form
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    global authenticated
    if request.method == 'POST':
        # Assume user logs in successfully
        authenticated = True
        flash("Logged in successfully!")

        # Check if there's an original POST request to handle
        if 'original_post' in session:
            data = session.pop('original_post')
            return handle_post(data)  # Process the original post request here

        return redirect(url_for('home'))

    return "Login Page"

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # The logic for handling the post request
    return "POST request processed!"

def handle_post(data):
    # Recreate the original POST request here
    # This example just returns the data as a string for demonstration
    return f"Processed original POST with data: {data}"

@app.route('/')
def home():
    return "Welcome Home!"

if __name__ == '__main__':
    app.run(debug=True)
