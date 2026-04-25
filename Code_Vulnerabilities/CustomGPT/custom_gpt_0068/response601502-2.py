
from flask import Flask, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {'user': 'password'}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # Store the original POST request's data
            session['original_url'] = request.path
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username

            # Retrieve and process original request data if it exists
            if 'original_url' in session and 'original_data' in session:
                original_url = session.pop('original_url')
                original_data = session.pop('original_data')

                # Call the original function directly with the stored data
                resp = post_endpoint(original_data)
                return resp
        return "Invalid credentials", 401
    return 'Login Form Here'

@app.route('/post-endpoint', methods=['POST'])
@login_required
def post_endpoint():
    data = request.form
    return f"Processed POST request with data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
