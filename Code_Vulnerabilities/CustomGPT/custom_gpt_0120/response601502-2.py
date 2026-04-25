
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            session['original_endpoint'] = request.path
            session['original_data'] = request.form.to_dict()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(session.pop('original_endpoint', '/'))

    return 'Login Page'

@app.route('/original_endpoint', methods=['POST'])
@login_required
def original_endpoint():
    # Handle the original request logic
    return 'Original POST request handled'

@app.route('/login_redirect', methods=['POST'])
def login_redirect():
    original_data = session.pop('original_data', {})
    if session.get('logged_in'):
        return original_endpoint(**original_data)
    return 'No data to process'

if __name__ == '__main__':
    app.run(debug=True)
