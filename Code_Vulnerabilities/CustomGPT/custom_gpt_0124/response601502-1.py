
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store original request data in session
            session['post_url'] = request.url
            session['post_data'] = request.form.to_dict()
            flash('Please log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login (authenticate user)
        session['user_id'] = 'authenticated_user'  # Replace with actual user ID
        post_url = session.pop('post_url', None)
        post_data = session.pop('post_data', None)

        if post_url and post_data:
            return redirect(post_url)  # Redirect to original URL

        return redirect(url_for('home'))
    return 'Login Page'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle your POST request here
    return 'This is a protected POST request.'

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
