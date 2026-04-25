
from flask import Flask, request, redirect, url_for, session, render_template, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'a_secure_random_key'

# Simulated user database
users = {'user': 'password'}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['logged_in'] = True
            next_url = session.pop('next_url', None)
            # Call original POST request if exists
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home'))
        else:
            flash('Invalid Credentials')
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the original POST request here
    data = request.form
    return f"Received data: {data}"

@app.before_request
def before_request():
    # Store POST data if user is not logged in
    if request.method == 'POST' and 'logged_in' not in session:
        session['next_url'] = request.path
        session['post_data'] = request.form.to_dict()

if __name__ == '__main__':
    app.run(debug=True)
