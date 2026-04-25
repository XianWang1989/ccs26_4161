
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            session['original_post'] = {
                'url': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['logged_in'] = True
        flash('Logged in successfully!')

        # Check if there was an original POST request to handle
        if 'original_post' in session:
            original_post = session.pop('original_post')
            return process_post(original_post['url'], original_post['data'])

        return redirect(url_for('home'))
    return 'Login Form'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # This function would only be called if logged in
    return 'You accessed the protected route!'

def process_post(url, data):
    # Simulate processing the POST request
    # You may want to validate the URL and data here
    if url == '/protected':
        # Call the original protected function if needed
        return protected()
    return 'Invalid request!'

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
