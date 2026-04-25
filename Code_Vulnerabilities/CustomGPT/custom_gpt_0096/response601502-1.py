
from flask import Flask, request, session, redirect, url_for, flash, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data
            session['post_data'] = request.form.to_dict()
            session['original_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        session['user_id'] = 'example_user'  # Assume user is authenticated
        flash('Login successful!')

        # Check if there's a stored request
        if 'post_data' in session:
            # Process the original POST request
            post_data = session.pop('post_data')
            # Handle the post data (e.g., call the original route)
            return handle_post(post_data)

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/your_protected_post', methods=['POST'])
@login_required
def your_protected_post():
    # Your POST request logic here
    return jsonify(message='Success!')

def handle_post(data):
    # Assuming the original route is `your_protected_post`
    return jsonify(message='Processed Post!', data=data)

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
