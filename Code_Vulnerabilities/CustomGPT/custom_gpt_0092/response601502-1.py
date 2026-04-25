
from flask import Flask, request, redirect, session, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login method (replace with real authentication)
def login_user(username, password):
    # Check credentials and log user in
    return True  # Or False if credentials are invalid

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original POST data in session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            session['user_id'] = username  # Set user as logged in

            # Replay the POST request if post_data exists
            if 'post_data' in session:
                post_data = session.pop('post_data')
                return redirect(url_for('handle_post', **post_data))
            return redirect(url_for('home'))  # Redirect to home or dashboard
    return 'Login Page'

@app.route('/handle_post', methods=['POST'])
@login_required
def handle_post():
    # Handle the actual POST request
    data = request.form
    return f"Data received: {data}"

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
