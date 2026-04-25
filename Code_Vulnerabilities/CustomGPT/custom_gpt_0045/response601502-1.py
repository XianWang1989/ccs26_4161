
from flask import Flask, request, redirect, url_for, session, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock authentication setup
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store POST data in session before redirecting to login
            session['original_request'] = (request.url, request.form)
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would normally verify username and password
        session['user_id'] = request.form['username']  # Mock login
        flash('Logged in successfully.')

        # Check if there was an original request stored
        if 'original_request' in session:
            original_url, original_data = session.pop('original_request')
            # Perform the original POST request with the saved data
            return redirect(original_url)

        return redirect(url_for('home'))  # Redirect to home if no original request

    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the post request here
    data = request.form['data']
    return f'Protected POST request processed with data: {data}'

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
