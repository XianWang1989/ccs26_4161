
from flask import Flask, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Save the original request information
            session['request_method'] = request.method
            session['request_data'] = request.form.to_dict()
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume authentication logic here
        session['user_id'] = 'some_user_id'  # Set user identifier on successful login
        flash('Logged in successfully!')

        # Check for any pending POST request
        if 'request_method' in session and session['request_method'] == 'POST':
            return handle_post_request(session['request_data'])  # Re-execute the request

        return redirect(url_for('index'))  # Redirect to main page after login
    return 'Login Form Here'  # Display your login form

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle your protected POST request here
    return "This is a protected POST request."

def handle_post_request(data):
    # Process the data that was pending from the POST request
    # For example, redirecting to the protected route and executing the required logic
    return "Re-executed POST request with data: " + str(data)

@app.route('/')
def index():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
