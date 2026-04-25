
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock function to check if user is logged in
def is_logged_in():
    return 'user_id' in session

# Decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store original request data in session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        session['user_id'] = 'some_user_id'  # Set user_id on successful login
        flash("Login successful!")

        # Check if there is POST data to process
        post_data = session.pop('post_data', None)
        if post_data:
            return redirect(url_for('handle_post', **post_data))

        return redirect(url_for('home'))

    return "<form method='post'>Login Form Here</form>"

@app.route('/protected', methods=['POST'])
@login_required
def handle_post():
    # This function will process the POST request
    data = request.form
    return f"Processed data: {data}"

@app.route('/home')
def home():
    return "Welcome Home!"

if __name__ == '__main__':
    app.run(debug=True)
