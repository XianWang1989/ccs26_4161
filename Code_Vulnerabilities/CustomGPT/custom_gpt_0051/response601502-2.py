
from flask import Flask, request, session, redirect, url_for
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            session['original_post'] = {
                'path': request.path,
                'data': request.form.to_dict()
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        # Execute the stored original POST if available
        original_post = session.pop('original_post', None)
        if original_post:
            return app.view_functions[original_post['path'].lstrip('/')](
                **original_post['data']
            )
        return redirect(url_for('index'))
    return "Login Page"

@app.route('/protected', methods=['POST'])
@login_required
def protected():
    # Process the POST request
    return "Protected POST Request Handled"

@app.route('/')
def index():
    return "Home Page"

if __name__ == '__main__':
    app.run()
