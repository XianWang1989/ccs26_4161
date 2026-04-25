
from flask import Flask, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the original request data in session
            session['original_method'] = request.method
            session['original_path'] = request.path
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for logging in
    if request.method == 'POST':
        # Authenticate user...
        session['logged_in'] = True

        # If user is authenticated, check for the original request
        if 'original_method' in session and session['original_method'] == 'POST':
            # Fetch original request data
            original_data = session.pop('original_data', {})
            session.pop('original_path', None)
            session.pop('original_method', None)

            # Execute the original POST request
            return original_post_handler(original_data)
        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    data = request.form
    return jsonify(success=True, data=data)

def original_post_handler(data):
    # Handle the original POST logic here
    return jsonify(success=True, data=data)

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
