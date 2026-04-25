
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            session['redirect_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login logic
    if request.method == 'POST':
        # Assume user is logged in successfully
        session['logged_in'] = True
        redirect_url = session.pop('redirect_url', None)
        return redirect(redirect_url or url_for('index'))
    return "Login Page"

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Process the POST request
    return "Protected POST Request Handled"

@app.route('/handle_post', methods=['POST'])
def handle_post():
    if 'logged_in' not in session:
        # Store POST data in session
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login'))
    # Access the POST data if user is logged in
    return protected()

@app.route('/')
def index():
    return "Home Page"

if __name__ == '__main__':
    app.run()
