
from flask import Flask, request, redirect, url_for, session, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request URL and form data in session
            session['next_url'] = request.path
            session['form_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle authentication here
        session['user_id'] = 'authenticated_user'  # Stub: replace with actual user id
        next_url = session.pop('next_url', None)
        form_data = session.pop('form_data', None)

        if next_url and form_data:
            return redirect(next_url)  # Redirect to the original URL
        return redirect(url_for('index'))  # Default redirect after login
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST data here
    data = request.form
    return jsonify(success=True, data=data)

@app.route('/')
def index():
    return 'Welcome to the homepage.'

if __name__ == '__main__':
    app.run()
