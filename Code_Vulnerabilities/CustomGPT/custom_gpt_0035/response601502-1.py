
from flask import Flask, request, session, redirect, url_for, flash
from flask import render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for session management

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            session['next_url'] = request.path  # Store the next URL
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here (authentication)
        session['logged_in'] = True
        next_url = session.get('next_url')
        session.pop('next_url', None)  # Clear next_url
        return redirect(next_url or url_for('home'))
    return render_template('login.html')

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    data = request.form
    # Here you can handle the POST data securely after login
    return f"Data received: {data}"

@app.route('/')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)
