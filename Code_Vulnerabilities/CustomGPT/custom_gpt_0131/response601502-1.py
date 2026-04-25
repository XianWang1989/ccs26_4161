
from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def login_required(f):
    def decorator(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the request data in session
            session['requested_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorator

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implement your login logic here
    if request.method == 'POST':
        # authenticate user and set session
        session['logged_in'] = True
        # Check if there is a requested URL after login
        requested_url = session.pop('requested_url', None)
        if requested_url:
            return redirect(requested_url)
        return redirect(url_for('home'))
    return "Login Page"

@app.route('/do_something', methods=['POST'])
@login_required
def do_something():
    # This function will handle the POST request
    data = request.form
    # Process the data
    return "Successfully handled POST request!"

if __name__ == "__main__":
    app.run(debug=True)
