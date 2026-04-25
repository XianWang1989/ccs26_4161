
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a real secret key

# Dummy user for demonstration
users = {'username': 'password'}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # Store request data before redirecting
            session['post_data'] = request.form.to_dict()  # Store all form data
            session['redirect_url'] = request.path
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
            # Redirect to the original URL
            redirect_url = session.pop('redirect_url', url_for('home'))
            return redirect(redirect_url)
        flash('Invalid credentials')
    return '<form method="post">Username: <input name="username"><br>Password: <input name="password"><br><button type="submit">Login</button></form>'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request after login
    data = request.form.to_dict()
    return f"Protected POST request succeeded! Data: {data}"

@app.route('/')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
