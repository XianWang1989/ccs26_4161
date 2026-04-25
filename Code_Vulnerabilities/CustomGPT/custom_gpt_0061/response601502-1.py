
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to log in first.')
            # Store the original POST data in the session
            if request.method == 'POST':
                session['original_post'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for validating login credentials
        # If login is successful:
        session['user_id'] = 'some_user_id'
        flash('Logged in successfully!')

        # Check if there is an original POST request to handle
        if 'original_post' in session:
            # Extract and clear original POST data
            original_data = session.pop('original_post')
            return handle_original_post(original_data)

        return redirect(url_for('home'))

    return 'Login Page'

@app.route('/some_protected_route', methods=['POST'])
@login_required
def some_protected_route():
    # Handle the POST request normally if logged in
    data = request.form
    return f'Handled POST request with {data}'

def handle_original_post(data):
    # This function handles the original POST request
    return f'Executed original POST request with {data}'

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
