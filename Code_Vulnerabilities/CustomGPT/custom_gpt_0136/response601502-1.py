
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Store the original request for replay
            if request.method == 'POST':
                session['post_data'] = request.form.to_dict()
                session['post_path'] = request.path
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        session['user_id'] = 'some_user_id'  # Example user_id on successful login
        post_data = session.pop('post_data', None)
        post_path = session.pop('post_path', None)

        if post_data and post_path:
            return redirect(url_for(post_path, **post_data))
        return redirect(url_for('home'))

    return '<form method="POST">Login Form Here</form>'

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the post request here
    return "Post request processed!"

@app.route('/home')
def home():
    return "Welcome Home!"

if __name__ == '__main__':
    app.run(debug=True)
