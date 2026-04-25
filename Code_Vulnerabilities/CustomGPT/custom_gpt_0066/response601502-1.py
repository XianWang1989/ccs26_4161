
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            session['next_request'] = {
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Suppose you've verified user credentials successfully
        session['logged_in'] = True
        flash('Logged in successfully!')

        # Check for any stored POST request
        next_request = session.pop('next_request', None)
        if next_request:
            # Execute the stored POST request
            return redirect(next_request['path'] + '?' + '&'.join(f"{k}={v}" for k, v in next_request['data'].items()))
        return redirect(url_for('home'))
    return "Login Form Here"  # Render your login form

@app.route('/some_post_endpoint', methods=['POST'])
@login_required
def some_post_endpoint():
    # Handle the original POST request
    data = request.form
    return f"Data received: {data}"

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
