
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample user database
users = {"user": "password"}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username
            next_url = session.pop('next_url', None)
            return redirect(next_url or url_for('home'))
        flash('Invalid credentials')
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    data = request.form.get('data')
    # Process your POST data here
    return f'POST data processed: {data}'

@app.route('/protected-post', methods=['POST'])
def protected_post():
    if 'username' not in session:
        # Store the original request data
        session['next_url'] = request.url
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login'))
    return post_endpoint()

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
