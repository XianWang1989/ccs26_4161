
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            session['original_request'] = {
                'path': request.path,
                'method': request.method,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for authenticating user
        session['logged_in'] = True
        flash('You are logged in.')

        # Check if there's an original request to process
        original_request = session.pop('original_request', None)
        if original_request:
            return redirect(original_request['path'])
        return redirect(url_for('home'))
    return 'Login Form'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Process the POST request
    data = request.form
    return f"Protected data processed: {data}"

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
