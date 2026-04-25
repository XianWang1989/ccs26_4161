
from flask import Flask, session, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            session['next_url'] = request.url  # Store the requested URL
            flash('Please log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume we validate and log the user in here
        session['user_id'] = 'some_user_id'

        # Redirect to the original request if it exists
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('home'))
    return 'Login Form Here'

@app.route('/protected_post', methods=['POST'])
@login_required
def protected_post():
    # Handle the POST request. This will be reached after the user is logged in.
    data = request.form
    # Process your data here
    return 'Form submitted successfully!', 200

@app.route('/submit_form', methods=['POST'])
@login_required
def submit_form():
    # Capture the requested data before redirecting
    session['post_data'] = request.form
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
