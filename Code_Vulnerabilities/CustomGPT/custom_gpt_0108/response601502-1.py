
from flask import Flask, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data in session
            if request.method == 'POST':
                session['post_data'] = request.form.to_dict()
                return redirect(url_for('login'))
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user logic here
        session['user_id'] = 'authenticated_user_id'  # Set user ID on successful login
        flash('Logged in successfully!')

        # Re-execute original POST request if available
        if 'post_data' in session:
            post_data = session.pop('post_data')  # Get original POST data
            return handle_post_request(post_data)  # Call the original handler

        return redirect(url_for('home'))  # Redirect to a default page

    return '<form method="post">Login Form</form>'  # Replace with your login form

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the original POST request here
    data = request.form
    return f"Data received: {data}"

def handle_post_request(post_data):
    # Manually create a request context to simulate the original POST
    with app.test_request_context('/post-endpoint', method='POST', data=post_data):
        return post_endpoint()

@app.route('/')
def home():
    return 'Welcome to the homepage!'

if __name__ == "__main__":
    app.run(debug=True)
