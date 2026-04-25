
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user database
users = {'user': 'password'}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # Store incoming request data
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            # Check if there's stored POST data to re-execute
            if 'post_data' in session:
                post_data = session.pop('post_data')
                return handle_post_request(post_data)  # Call your handler directly
            return redirect(url_for('home'))
    return 'Login Page'

@app.route('/post_endpoint', methods=['POST'])
@login_required
def handle_post_request():
    # Handle your POST request here
    data = request.form
    return jsonify({'message': 'POST request processed', 'data': data})

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
