
from flask import Flask, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user database
USERS = {'user': 'password'}

def login_required(f):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            session['post_data'] = request.form.to_dict()  # Store POST data
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__  # Allow for better debugging
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['username'] = username
            flash('Logged in successfully!')

            # Check if there's stored post data
            if 'post_data' in session:
                post_data = session.pop('post_data')  # Get and remove POST data
                return handle_post_request(post_data)  # Call the original POST request
            return redirect(url_for('home'))

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/original_post', methods=['POST'])
@login_required
def original_post_request():
    # Handle the actual POST request here
    data = request.form
    return f"Data received: {data}"

def handle_post_request(post_data):
    # Your logic to process the post_data
    return f"Data received after login: {post_data}"

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
