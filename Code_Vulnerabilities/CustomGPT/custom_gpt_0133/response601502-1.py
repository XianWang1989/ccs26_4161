
from flask import Flask, request, redirect, session, url_for, flash, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session management

# Dummy user store
users = {'user': 'password'}  # Replace with proper user authentication logic

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store request method and data in session
            if request.method == 'POST':
                session['post_data'] = request.form.to_dict()  # Store POST data
            return redirect(url_for('login'))  # Redirect to login
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['logged_in'] = True
            flash('Login Successful!')

            # Check for stored POST data
            if 'post_data' in session:
                post_data = session.pop('post_data')  # Retrieve and remove from session
                return execute_post_request(post_data)  # Execute the appropriate logic

            return redirect(url_for('home'))  # Go to home page if no POST data
        flash('Invalid credentials!')
    return '''<form method="post">
                Username: <input type="text" name="username">
                Password: <input type="password" name="password">
                <input type="submit" value="Login">
              </form>'''

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle your post logic here
    return jsonify({"status": "success", "data": request.form}), 200

def execute_post_request(post_data):
    # Here you can handle the logic of the POST request
    # For demonstration, we'll just return the data as a response
    return jsonify({"status": "executed", "data": post_data}), 200

@app.route('/home')
@login_required
def home():
    return "Welcome to the protected home page!"

if __name__ == '__main__':
    app.run(debug=True)
