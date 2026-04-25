
from flask import Flask, redirect, request, session, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request data
            session['original_post'] = {
                'url': request.url,
                'data': request.form
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here (check credentials, etc.)
        session['user_id'] = 'some_user_id'  # Example user ID
        original_post = session.pop('original_post', None)

        if original_post:
            # Re-execute the original POST request
            return handle_post_request(original_post['data'])

        return redirect(url_for('home'))

    return '<form method="POST">Login Form</form>'  # Placeholder for actual login form

@app.route('/your_post_endpoint', methods=['POST'])
@login_required
def handle_post_request():
    # Handle your POST request logic here
    data = request.form
    return f"Data received: {data}"

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
