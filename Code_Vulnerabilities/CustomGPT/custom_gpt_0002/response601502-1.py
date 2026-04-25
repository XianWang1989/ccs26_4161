
from flask import Flask, request, session, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            session['next_url'] = request.url
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform login logic here
        session['user_id'] = 'user-id'  # Simulate user login
        next_url = session.pop('next_url', None)
        if next_url:
            return redirect(next_url)
    return 'Login Form'

@app.route('/protected-post', methods=['POST'])
@login_required
def protected_post():
    # Capture original request data
    session['post_data'] = request.form.to_dict()
    return 'Protected POST executed'

@app.route('/execute-post')
def execute_post():
    if 'post_data' in session:
        post_data = session.pop('post_data')
        response = requests.post('http://yourapi.com/protected-post', data=post_data)
        return response.text
    return 'No POST data found'

if __name__ == '__main__':
    app.run(debug=True)
