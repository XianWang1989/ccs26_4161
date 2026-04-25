
from flask import Flask, request, redirect, session, url_for, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request details
            session['original_request'] = {
                'method': request.method,
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate user
        session['user_id'] = 'some_user_id'  # Set user id after login
        # Redirect back to necessary POST request if exists
        original_request = session.pop('original_request', None)
        if original_request and original_request['method'] == 'POST':
            return post_handler(original_request['data'])  # Call the POST handler
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_handler():
    # Handle the original POST request
    data = request.form
    # Do something with the data
    return "Data submitted successfully!"

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
