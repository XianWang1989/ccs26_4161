
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # If user is not logged in, store the original request data
            session['orig_post_data'] = request.form.to_dict()
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Authenticate the user
        session['user_id'] = 'authenticated_user'  # Example authentication
        flash('Login successful.')
        # Retrieve original POST data after successful login
        orig_post_data = session.pop('orig_post_data', None)
        if orig_post_data:
            return redirect(url_for('handle_post', **orig_post_data))
        return redirect(url_for('home'))
    return '<form method="post">Login Form</form>'

@app.route('/post_data', methods=['POST'])
@login_required
def handle_post():
    data = request.form
    # Process the POST data here
    return f'Handled POST with data: {data}'

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
