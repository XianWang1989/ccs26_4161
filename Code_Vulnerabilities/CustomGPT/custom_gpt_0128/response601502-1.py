
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data in the session
            session['post_data'] = request.form.to_dict()  # Capture POST data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you handle user authentication
        # Assuming successful login:
        session['user_id'] = 'example_user'  # Set user_id in session
        post_data = session.pop('post_data', None)  # Get and remove post data

        if post_data:
            # Execute the original POST request logic
            return execute_post_request(post_data)

        return redirect(url_for('home'))  # Redirect to homepage if no post data
    return 'Login Page'

@app.route('/some_post_endpoint', methods=['POST'])
@login_required
def some_post_endpoint():
    # Example POST request logic
    data = request.form
    return jsonify(data), 200

def execute_post_request(post_data):
    # Here you can manually call the original endpoint logic using the stored data
    # For example:
    response_data = {"status": "success", "data": post_data}
    return jsonify(response_data), 200

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
