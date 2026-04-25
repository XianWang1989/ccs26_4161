
from flask import Flask, session, redirect, request, url_for, render_template
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated login state
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implementation of login logic
    if request.method == 'POST':
        # Assume user is authenticated
        session['logged_in'] = True
        return redirect(session.pop('next_url', '/'))
    return render_template('login.html')

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            session['next_url'] = request.url  # Store the requested URL
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/post_data', methods=['POST'])
@login_required
def post_data():
    # Handle your POST request here
    data = request.form.get('data')
    return f'You posted: {data}'

@app.route('/handle_post', methods=['POST'])
def handle_post():
    # If not logged in, this will redirect to login
    return post_data()

if __name__ == "__main__":
    app.run(debug=True)
