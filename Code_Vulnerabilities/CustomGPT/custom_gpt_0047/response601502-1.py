
from flask import Flask, request, session, redirect, url_for, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store original POST data if login is required
            if request.method == 'POST':
                session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        session['logged_in'] = True
        # After login, check for stored POST data
        if 'post_data' in session:
            post_data = session.pop('post_data')  # Remove from session
            # Now, call the original endpoint
            return original_post_request_handler(post_data)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/original-post', methods=['POST'])
@login_required
def original_post_request_handler():
    # Handle the original POST request
    return "POST request was successfully processed!"

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
