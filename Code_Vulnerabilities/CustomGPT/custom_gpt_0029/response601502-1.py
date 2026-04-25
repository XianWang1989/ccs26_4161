
from flask import Flask, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate successful login
        session['logged_in'] = True
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('home'))
    return 'Login Form Here'

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the POST request
    data = request.form.get('data')
    return f'POST data received: {data}'

@app.route('/protected_route', methods=['POST'])
def protected_route():
    if 'logged_in' not in session:
        session['next_url'] = request.url
        session['post_data'] = request.form.to_dict()
        return redirect(url_for('login'))

    data = request.form.get('data')
    return f'POST data processed: {data}'

@app.route('/execute_post', methods=['POST'])
@login_required
def execute_post():
    if 'post_data' in session:
        data = session.pop('post_data')
        # Execute the original POST request logic here
        return f'Executed POST with data: {data}'
    return 'No data to process.'

if __name__ == '__main__':
    app.run(debug=True)
