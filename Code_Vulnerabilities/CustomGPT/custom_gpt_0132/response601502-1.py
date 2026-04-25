
from flask import Flask, session, request, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            # Store original request data before redirecting
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['user'] = request.form['username']  # Simplified for illustration
        flash('Logged in successfully!')

        # After login, check for stored request data
        post_data = session.pop('post_data', None)
        if post_data:
            # You can now Process the stored POST data
            return handle_post_request(post_data)

        return redirect(url_for('home'))

    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the POST request normally
    return 'Handled POST request'

def handle_post_request(data):
    # Process the previously stored post data
    # e.g., saving to database, etc.
    return f'Processed POST data: {data}'

@app.route('/')
def home():
    return 'Welcome to the Home Page'

if __name__ == '__main__':
    app.run(debug=True)
