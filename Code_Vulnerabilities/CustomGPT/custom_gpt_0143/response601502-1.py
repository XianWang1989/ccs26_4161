
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            # Store request data in session
            session['next_url'] = request.path
            session['request_method'] = 'POST'
            session['request_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic
        session['logged_in'] = True
        # Redirect to stored URL
        next_url = session.get('next_url')
        if next_url and session.get('request_method') == 'POST':
            return redirect(next_url)
        return redirect(url_for('home'))
    return "Login Page"

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the POST request
    data = request.form
    return "Data processed: " + str(data)

@app.route('/home')
def home():
    return "Welcome Home!"

if __name__ == '__main__':
    app.run(debug=True)
