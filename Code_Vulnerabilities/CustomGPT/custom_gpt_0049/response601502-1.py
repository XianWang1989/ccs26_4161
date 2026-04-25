
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data in session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implement your login logic here
    # On successful login:
    session['user_id'] = 'some_user_id'  # Adjust based on your login method
    post_data = session.pop('post_data', None)
    if post_data:
        # Re-execute the stored POST request
        return handle_post_request(post_data)
    return "Welcome! Please log in."

@app.route('/protected_post', methods=['POST'])
@login_required
def handle_post_request():
    # Handle the POST request here
    data = request.form
    # Process the data
    return "Data processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
