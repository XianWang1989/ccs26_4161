
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Simulated user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original POST data if it's a POST request
            if request.method == 'POST':
                session['original_post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dummy login logic
        session['user_id'] = 'some_user_id'  # This should be user-specific
        # Check if there's original POST data to process
        if 'original_post_data' in session:
            original_data = session.pop('original_post_data')
            # Execute the original POST request here, e.g., call the function directly
            return handle_original_post(original_data)
        return redirect(url_for('home'))
    return 'Login Form'

@app.route('/api/resource', methods=['POST'])
@login_required
def protected_resource():
    # If user is authenticated, this will be accessed normally
    return jsonify({"status": "Success", "data": request.form})

def handle_original_post(data):
    # Handle the POST data (similar to the protected_resource logic)
    return jsonify({"status": "Success", "data": data})

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
