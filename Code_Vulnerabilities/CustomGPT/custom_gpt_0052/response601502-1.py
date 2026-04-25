
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user store
users = {'username': 'password'}

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
        if username in users and users[username] == password:
            session['username'] = username
            next_url = request.args.get('next')
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home'))  # Redirect to default page
        flash('Invalid username/password')
    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/post_data', methods=['POST'])
@login_required
def post_data():
    # Process the data
    data = request.form.get('data')
    print(f'Data received: {data}')
    return 'Data processed', 200

@app.route('/handle_post', methods=['POST'])
def handle_post():
    # Store request data before redirecting to login
    session['post_data'] = request.form.to_dict()
    return redirect(url_for('login'))

@app.route('/data_process', methods=['GET'])
@login_required
def data_process():
    # Retrieve and process the stored POST data
    if 'post_data' in session:
        data = session.pop('post_data')  # Remove it from the session
        # Call the actual handler with the stored data
        return post_data()  # You can modify this to match your needs
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
