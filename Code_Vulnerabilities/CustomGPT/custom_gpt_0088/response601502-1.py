
from flask import Flask, request, redirect, session, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store the original request data
            session['original_data'] = request.form if request.method == 'POST' else None
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user (this is just a placeholder)
        session['logged_in'] = True
        flash('Login successful!')

        # Check if there was an original request
        original_data = session.pop('original_data', None)
        if original_data:
            return redirect(url_for('protected_route', **original_data))

        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected_route():
    # Handle the protected POST request
    # Use request.form to get the data
    return 'POST request successful!'

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
