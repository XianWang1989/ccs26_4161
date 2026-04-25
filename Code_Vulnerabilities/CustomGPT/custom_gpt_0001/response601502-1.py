
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login checker for demonstration
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request method and data
            session['original_url'] = request.url
            session['original_method'] = request.method
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        # If successful:
        session['user_id'] = 'user123'  # Set user's session

        # Check if there's a stored original request
        if 'original_url' in session:
            original_url = session.pop('original_url')
            original_data = session.pop('original_data', {})
            # Redirect back to original URL and call the function directly
            return handle_post_request(original_data)  # Call original function here
        return redirect(url_for('homepage'))

    return '<form method="post">Login Form</form>'

@app.route('/protected', methods=['POST'])
@login_required
def handle_post_request():
    data = request.form  # Your POST data processing logic
    return f'Handled POST request with data: {data}'

@app.route('/')
def homepage():
    return 'Welcome to the Homepage'

if __name__ == '__main__':
    app.run(debug=True)
