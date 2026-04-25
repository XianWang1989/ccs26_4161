
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:  # Check if user is logged in
            session['original_url'] = request.url  # Store original URL
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Your login logic goes here
        session['logged_in'] = True  # Set user as logged in
        flash('You were successfully logged in')

        # Check if there is stored POST data
        if 'original_url' in session:
            original_url = session.pop('original_url')  # Retrieve the original URL
            return redirect(original_url)  # Redirect back to the original URL
        return redirect(url_for('index'))  # Fallback route

    return 'Login Form Here'  # Render your login form

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # If user is logged in, this will execute
    data = request.form  # Your form data processing
    # Handle the data as needed
    return "Post Successful", 200

if __name__ == '__main__':
    app.run(debug=True)
