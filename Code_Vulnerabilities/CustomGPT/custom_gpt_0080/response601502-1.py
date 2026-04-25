
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        next_url = request.args.get('next')
        if next_url:
            return redirect(next_url)
        return redirect(url_for('home'))
    return "Login Form Here"

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle your POST request
    return "POST request handled!"

@app.route('/protected_post', methods=['POST'])
def protected_post():
    if 'logged_in' not in session:
        # Store the POST data in session
        session['post_data'] = request.form
        return redirect(url_for('login', next=request.url))

    # If authenticated, process the POST data directly
    return post_endpoint()

@app.route('/execute_post_after_login', methods=['POST'])
def execute_post_after_login():
    if 'post_data' in session:
        data = session.pop('post_data')  # Retrieve and remove post data from session
        # Optionally, handle the data as needed
        return f"Handled POST data: {data}"
    return redirect(url_for('home'))

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
