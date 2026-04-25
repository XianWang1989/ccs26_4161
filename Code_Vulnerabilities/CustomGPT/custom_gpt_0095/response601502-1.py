
from flask import Flask, request, session, redirect, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['next_post_data'] = {
                'path': request.path,
                'form_data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for authenticating user goes here
        session['user_id'] = 'valid_user_id'  # Simulating successful login
        # After logging in, check for stored POST request
        if 'next_post_data' in session:
            data = session.pop('next_post_data')
            return redirect(data['path'], code=303)  # Use 303 to indicate a GET redirect
    return '<form method="post">Login Form</form>'

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Handle the POST request
    data = request.form
    return f'Protected resource accessed with data: {data}'

if __name__ == '__main__':
    app.run(debug=True)
