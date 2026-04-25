
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Mock for checking if the user is logged in
def is_logged_in():
    return session.get('user_id') is not None

# Custom login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            # Store original POST data
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here...
        session['user_id'] = 'some_user_id'  # Set user ID upon successful login

        # After login, check if there's original data
        if 'original_data' in session:
            # Get stored data
            original_data = session.pop('original_data')
            # Reissue the POST request
            return handle_post_request(original_data)

        return redirect(url_for('home'))

    return "Login Page"

@app.route('/post-endpoint', methods=['POST'])
@login_required
def handle_post_request():
    # Handle your POST logic here
    return jsonify({"message": "Post request handled", "data": request.form})

@app.route('/')
def home():
    return "Welcome Home!"

if __name__ == '__main__':
    app.run(debug=True)
