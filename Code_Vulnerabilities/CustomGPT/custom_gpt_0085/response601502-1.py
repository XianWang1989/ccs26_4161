
from flask import Flask, request, redirect, session, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request path and form data
            session['original_request_path'] = request.path
            session['original_request_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        session['user_id'] = 'authenticated_user'  # Replace with actual authentication logic
        original_path = session.pop('original_request_path', None)
        original_data = session.pop('original_request_data', None)

        if original_path:
            # Re-execute the original POST request
            return redirect(original_path)  # use render_template for GET requests
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the protected POST request
    return 'This is a protected resource.'

if __name__ == '__main__':
    app.run(debug=True)
