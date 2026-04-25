
from flask import Flask, redirect, url_for, request, session, abort

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login_required(f):
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            # Store the original request method and data
            session['original_request'] = {
                'method': request.method,
                'data': request.form.to_dict(),
                'path': request.path
            }
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate login
        session['logged_in'] = True
        original_request = session.pop('original_request', None)

        # If there's an original request, handle it
        if original_request:
            return handle_post_request(original_request['path'], original_request['data'])

        return redirect(url_for('home'))

    return 'Login Page'

@app.route('/post_handler', methods=['POST'])
@login_required
def post_handler():
    # Handle the post request here
    return 'Post request processed'

def handle_post_request(path, data):
    with app.test_request_context(path, method='POST', data=data):
        return post_handler()

@app.route('/')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
