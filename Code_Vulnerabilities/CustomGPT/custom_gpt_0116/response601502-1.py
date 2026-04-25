
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user authentication
def is_logged_in():
    return 'user_id' in session

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            session['next_post_data'] = request.form.to_dict()
            session['next_post_url'] = request.path
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Your login logic here
        session['user_id'] = 'user'  # Example login
        next_post_data = session.pop('next_post_data', None)
        next_post_url = session.pop('next_post_url', None)

        # Handle the POST request if it exists
        if next_post_data and next_post_url:
            return redirect(url_for('handle_post', **next_post_data))

        return redirect(url_for('home'))

    return "Login Form"

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post():
    # Process your POST data here
    data = request.form
    return f"Data received: {data}"

@app.route('/protected_route', methods=['POST'])
@login_required
def protected_route():
    # Original protected POST route logic
    return "This is a protected route."

@app.route('/')
def home():
    return "Welcome to the Home Page."

if __name__ == '__main__':
    app.run(debug=True)
