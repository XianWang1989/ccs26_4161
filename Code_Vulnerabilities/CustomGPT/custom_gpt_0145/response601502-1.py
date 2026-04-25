
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login required decorator
def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'user' not in session:
            session['next_url'] = request.url  # Store the original URL
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorator

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login here (this is just a mock)
        session['user'] = 'user_id'  # Mark the user as logged in
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)  # Redirect back to original URL
        return redirect(url_for('home'))  # Or to a default page
    return '<form method="post">Login Form</form>'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # This is your protected POST endpoint
    data = request.form
    # Process data here
    return f'Success! Data received: {data}'

@app.route('/example', methods=['POST'])
@login_required
def example():
    # Another protected POST endpoint
    return "This endpoint is also protected."

if __name__ == "__main__":
    app.run(debug=True)
