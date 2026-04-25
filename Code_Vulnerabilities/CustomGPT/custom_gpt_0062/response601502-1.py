
from flask import Flask, request, redirect, url_for, session, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            # Store the request method and data in session
            session['original_request'] = {
                'method': request.method,
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here:
        session['logged_in'] = True
        # After logging in, check if there was an original request
        if 'original_request' in session:
            original_request = session.pop('original_request')
            if original_request['method'] == 'POST':
                return handle_post_request(original_request['data'])
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # This function will not be called unless logged in
    return 'This is a protected POST request.'

def handle_post_request(data):
    # Handle the original POST request here
    # For example, process the data and return a response
    return f"Processed data: {data}"

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
