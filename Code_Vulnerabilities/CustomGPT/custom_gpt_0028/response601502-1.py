
from flask import Flask, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    # A simple decorator to require login
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store original endpoint and POST data
            session['original_post_data'] = request.form.to_dict() if request.method == 'POST' else None
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['logged_in'] = True
        flash('Logged in successfully!')

        # Check for original POST data
        original_post_data = session.pop('original_post_data', None)
        if original_post_data:
            # Reprocess the original POST request
            return handle_post_request(original_post_data)

        return redirect(url_for('home'))  # Redirect to a homepage or desired route
    return 'Login Form'

@app.route('/protected', methods=['POST'])
@login_required
def handle_post_request(data=None):
    if data is None:
        data = request.form
    # Process the POST request here
    return f'Handled POST request with data: {data}'

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
