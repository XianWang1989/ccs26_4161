
from flask import Flask, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# A simple example user datastore
users = {
    'username': 'password'
}

# Mock login check (you should replace this with your real authentication logic)
def is_authenticated():
    return 'username' in session

def login_required(f):
    def wrapped(*args, **kwargs):
        if not is_authenticated():
            # Store the original request's data to the session
            session['post_data'] = request.form.to_dict()  # Save form data
            return redirect(url_for('login'))  # redirect to login
        return f(*args, **kwargs)
    return wrapped

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            session['username'] = username

            # After login, check for stored POST data
            post_data = session.pop('post_data', None)
            if post_data:
                # Re-execute the original POST request
                return original_post_request_handler(post_data)

            # Redirect to a default page upon successful login
            return redirect(url_for('home'))

        flash('Invalid credentials', 'error')

    return '''
    <form method="post">
        Username: <input type="text" name="username" required>
        Password: <input type="password" name="password" required>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the original POST request
    return 'Post request handled!'

def original_post_request_handler(post_data):
    # Here you would implement logic based on the original POST data received
    return f'Post request re-executed with: {post_data}'

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
