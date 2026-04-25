
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock function to check if user is authenticated
def is_authenticated():
    return 'user_id' in session

# Custom decorator for login protection
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            session['redirect_post'] = request.form.to_dict()  # Store form data
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Mock login process
        session['user_id'] = 'some_user_id'  # Authenticate user
        flash('Logged in successfully.')

        # Check if there is a stored POST data
        if 'redirect_post' in session:
            post_data = session.pop('redirect_post')  # Retrieve and remove the data
            return redirect(request.path)  # Redirect to original endpoint after login

    return '<form method="post">Login Form</form>'

@app.route('/submit', methods=['POST'])
@login_required
def submit_post():
    # Handle the POST request
    form_data = request.form
    return f"Data received: {form_data}"

if __name__ == '__main__':
    app.run(debug=True)
