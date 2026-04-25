
from flask import Flask, session, redirect, request, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store request data for later
            session['post_data'] = request.form
            session['return_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Implement your login logic here
        session['logged_in'] = True
        flash('Logged in successfully!')

        # Check if there's a stored POST request
        post_data = session.pop('post_data', None)
        return_url = session.pop('return_url', None)
        if post_data and return_url:
            # Re-execute the POST request
            return redirect(return_url)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/some_post_endpoint', methods=['POST'])
@login_required
def some_post_endpoint():
    # Handle the POST request
    data = request.form
    return f"Received data: {data}"

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
