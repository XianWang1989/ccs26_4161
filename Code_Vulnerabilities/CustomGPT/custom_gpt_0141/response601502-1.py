
from flask import Flask, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    """Decorator to ensure user is logged in."""
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request details
            session['original_post_data'] = {
                'url': request.path,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Mock login route."""
    if request.method == 'POST':
        # Here you would add your authentication logic
        session['user_id'] = 'some_user_id'  # Store user ID in session
        # Check if there’s an original post request to process
        original_post = session.pop('original_post_data', None)
        if original_post:
            return redirect(original_post['url'])
        return redirect(url_for('homepage'))
    return '<form method="post">Login Form</form>'

@app.route('/protected-endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    """A protected POST endpoint."""
    data = request.form
    # Process the data
    return jsonify({"message": "Success", "data": data})

@app.route('/')
def homepage():
    return '<h1>Welcome to the Homepage</h1>'

if __name__ == '__main__':
    app.run(port=8080)
