
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login status
user_logged_in = False

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not user_logged_in:
            # Store the original request data in the session
            session['original_request'] = {
                'url': request.url,
                'method': request.method,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    global user_logged_in
    if request.method == 'POST':
        # Perform login logic here
        user_logged_in = True
        flash('Login successful!')

        # After login, check for an original request
        original_request = session.pop('original_request', None)
        if original_request:
            return handle_post_request(original_request['data'])

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the post request logic here
    return 'POST request handled'

def handle_post_request(data):
    # This function handles executing the original post request
    # Here you could create a response as if it was handled by the usual route
    return f'POST request successfully executed with data: {data}'

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
