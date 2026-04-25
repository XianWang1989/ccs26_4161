
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store the original POST data in session
            session['post_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform authentication (this is just a placeholder example)
        session['logged_in'] = True
        flash('Logged in successfully!')

        # After login, check and execute stored POST request
        if 'post_data' in session:
            post_data = session.pop('post_data')
            return handle_post_data(post_data)

        return redirect(url_for('home'))

    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    data = request.form
    return f'Protected data processed: {data}'

def handle_post_data(data):
    # Process the POST data as required
    return f'Handled POST after login: {data}'

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
