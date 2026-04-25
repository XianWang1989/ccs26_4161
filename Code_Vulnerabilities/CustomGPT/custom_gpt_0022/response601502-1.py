
from flask import Flask, request, session, redirect, url_for, jsonify, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock login function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            # Save the original request method and data
            session['post_data'] = request.form.to_dict()
            flash('You need to log in first!')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume successful login
        session['user_id'] = 'logged_in_user'
        post_data = session.pop('post_data', None)
        if post_data:
            # Redirect back to the original POST request after login
            return redirect(url_for('handle_post', **post_data))
        return redirect(url_for('home'))
    return '''<form method="post">Login <input type="submit"></form>'''

@app.route('/post_endpoint', methods=['POST'])
@login_required
def handle_post():
    # Handle the POST request
    data = request.form
    return jsonify(data)

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
