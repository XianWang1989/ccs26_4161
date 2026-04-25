
from flask import Flask, request, session, redirect, url_for, render_template, jsonify
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store request data for POST requests
            if request.method == 'POST':
                session['original_url'] = request.path
                session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for user authentication
        session['logged_in'] = True
        # Execute original POST request if exists
        if session.get('original_url'):
            post_data = session.get('post_data')
            return redirect(session['original_url'], code=303)
    return render_template('login.html')

@app.route('/do_something', methods=['POST'])
@login_required
def do_something():
    # Handle your POST logic here
    data = request.form
    return jsonify(success=True, data=data)

@app.route('/')
def home():
    return '<a href="/some_post_endpoint">Make a POST request</a>'

if __name__ == '__main__':
    app.run(debug=True)
