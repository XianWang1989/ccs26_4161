
from flask import Flask, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user store
users = {'username': generate_password_hash('password')}

# Login required decorator
def login_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            session['next_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user, password):
            session['user_id'] = username
            next_url = session.pop('next_url', url_for('home'))
            return redirect(next_url)
        flash('Invalid credentials')
    return '<form method="post">Username: <input type="text" name="username"><br>Password: <input type="password" name="password"><br><input type="submit"></form>'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle your POST request logic here
    data = request.form
    return f"Data received: {data}"

@app.route('/protected-post', methods=['POST'])
@login_required
def protected_post():
    session['post_data'] = request.form.to_dict()  # Store the POST data
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
