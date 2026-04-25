
from flask import Flask, request, session, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['next_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_id'] = 'user_id_here'  # Authenticate user
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('home'))
    return 'Login Form'

@app.route('/submit', methods=['POST'])
@login_required
def submit():
    data = request.form['data']
    # Process the data here
    return 'Data submitted: ' + data

if __name__ == '__main__':
    app.run(debug=True)
