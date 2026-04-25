
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulate a user authentication check
def is_authenticated():
    return session.get('user_authenticated', False)

# Decorator to protect routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            # Store the request method and data
            session['original_url'] = request.url
            session['original_method'] = request.method
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate the user (placeholder logic)
        session['user_authenticated'] = True
        flash('Logged in successfully!')

        # After logging in, check if there's a stored request
        original_url = session.pop('original_url', None)
        original_method = session.pop('original_method', None)
        original_data = session.pop('original_data', None)

        if original_url and original_method == 'POST':
            return redirect(original_url)  # For simplicity, just redirecting

        return redirect(url_for('index'))

    return '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the original POST request here
    return "Protected content accessed!"

@app.route('/')
def index():
    return 'Welcome!'

if __name__ == '__main__':
    app.run(debug=True)
