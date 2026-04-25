
from flask import Flask, request, redirect, session, url_for, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user login status
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate a successful login
        session['user'] = 'username'
        original_post_data = session.pop('original_post_data', None)
        if original_post_data:
            return redirect(url_for(original_post_data['route'], **original_post_data['data']))
        return redirect(url_for('home'))
    return 'Login Form'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            # Save original POST data in session
            if request.method == 'POST':
                session['original_post_data'] = {
                    'route': request.path,
                    'data': request.form.to_dict()
                }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/post_endpoint', methods=['POST'])
@login_required
def post_endpoint():
    # Handle the POST request logic
    return 'Data submitted: {}'.format(request.form)

@app.route('/')
def home():
    return 'Home Page. <a href="/post_endpoint">Post Data</a>'

if __name__ == '__main__':
    app.run(debug=True)
