
from flask import Flask, session, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the original request method and form data
            session['post_request'] = {
                'url': request.path,
                'form': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume a successful login process
        session['logged_in'] = True
        flash('Login successful!')

        # Check for stored POST request after login
        if 'post_request' in session:
            post_request = session.pop('post_request')
            # Here you can trigger the original POST request
            return handle_post_request(post_request['url'], post_request['form'])

        return redirect(url_for('home'))

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Log in">
        </form>
    '''

def handle_post_request(url, data):
    # Here you would typically handle the original POST request logic
    if url == '/some_protected_endpoint':
        # Process the stored form data
        return f"Handled POST request to {url} with data: {data}"

@app.route('/some_protected_endpoint', methods=['POST'])
@login_required
def protected_endpoint():
    return "This is a protected endpoint."

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
