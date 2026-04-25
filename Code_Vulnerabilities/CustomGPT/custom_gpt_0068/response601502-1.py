
from flask import Flask, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user store
users = {'user': 'password'}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # Store original form data
            session['original_form'] = request.form.to_dict() 
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username
            # After login, check if there's an original form action
            if 'original_form' in session:
                original_form = session.pop('original_form')
                # Here you would handle the original POST data
                # e.g., process_form(original_form)
                return "Logged in and original form processed!"
        return "Invalid credentials", 401
    return 'Login Form Here'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Your original POST logic would be implemented here.
    return "This is a protected POST endpoint."

if __name__ == '__main__':
    app.run(debug=True)
