
from flask import Flask, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data
            session['post_data'] = request.form.to_dict()  # Store as dictionary
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming user authentication is successful
        session['user_id'] = 'user_identifier'  # Replace with actual user ID
        return redirect(url_for('post_handler'))

    return "Login Form"  # Render your login form here

@app.route('/post-handler', methods=['POST'])
@login_required
def post_handler():
    # Handle the POST request
    return jsonify({"message": "POST request successful", "data": request.form})

@app.route('/execute-post', methods=['POST'])
@login_required
def execute_post():
    # If login is required, handle and store post data
    return post_handler()

@app.route('/process-login', methods=['POST'])
def process_login():
    # Check credentials and log in user...
    # After logging in:
    post_data = session.pop('post_data', None)
    if post_data:
        # Process the original POST request
        with app.test_request_context('/post-handler', method='POST', data=post_data):
            return post_handler()
    return redirect(url_for('home'))

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
